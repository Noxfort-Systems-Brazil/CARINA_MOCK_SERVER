import time
import threading
from src.core.telemetry_state import TelemetryState

class MockEdgeState:
    def __init__(self, occupancy=0.0, mean_speed=0.0, queue_length=0, density=0.0):
        self.occupancy = occupancy
        self.mean_speed = mean_speed
        self.queue_length = queue_length
        self.density = density

def test_telemetry_initial_state():
    telemetry = TelemetryState(max_events=5)
    snap = telemetry.get_snapshot()

    assert not snap.connected
    assert snap.server_state == "IDLE"
    assert snap.total_frames == 0
    assert snap.frame_rate_hz == 0.0
    assert snap.all_zeros is True
    assert len(snap.recent_events) >= 1

def test_record_ping():
    telemetry = TelemetryState()
    telemetry.record_ping()
    snap = telemetry.get_snapshot()

    assert snap.connected
    assert snap.last_ping_time is not None
    assert snap.time_since_last_ping is not None
    assert any("Ping recebido" in event for event in snap.recent_events)

def test_record_scenario():
    telemetry = TelemetryState()
    telemetry.record_scenario(
        map_hash="hash_123",
        map_name="test_city.net.xml",
        file_size=2048,
        nodes=100,
        edges=250
    )
    snap = telemetry.get_snapshot()

    assert snap.scenario_loaded
    assert snap.map_hash == "hash_123"
    assert snap.map_name == "test_city.net.xml"
    assert snap.file_size_bytes == 2048
    assert snap.nodes_count == 100
    assert snap.edges_count == 250
    assert snap.server_state == "READY"
    assert any("Cenário carregado" in event for event in snap.recent_events)

def test_record_control():
    telemetry = TelemetryState()
    telemetry.record_control("START", "RUNNING")
    snap = telemetry.get_snapshot()

    assert snap.server_state == "RUNNING"
    assert any("Comando: START -> Estado: RUNNING" in event for event in snap.recent_events)

def test_record_traffic_frame_heartbeat():
    telemetry = TelemetryState()
    # sequence_id 0 or empty dictionary is heartbeat
    telemetry.record_traffic_frame(sequence_id=0, timestamp=1.0, edges_dict={})
    snap = telemetry.get_snapshot()

    assert snap.connected
    assert snap.total_frames == 0  # Heartbeat does not increment total_frames

def test_record_traffic_frame_active_data():
    telemetry = TelemetryState()

    edges = {
        "e1": MockEdgeState(occupancy=0.5, mean_speed=10.0, queue_length=3, density=0.2),
        "e2": MockEdgeState(occupancy=0.9, mean_speed=2.0, queue_length=15, density=0.8),
        "e3": MockEdgeState(occupancy=0.0, mean_speed=0.0, queue_length=0, density=0.0),
    }

    telemetry.record_traffic_frame(sequence_id=1, timestamp=10.0, edges_dict=edges)
    snap = telemetry.get_snapshot()

    assert snap.total_frames == 1
    assert snap.last_sequence_id == 1
    assert snap.last_timestamp == 10.0
    assert snap.all_zeros is False
    assert snap.total_edges_in_frame == 3
    assert snap.active_edges_count == 2
    assert snap.max_occupancy == 0.9
    assert snap.max_queue == 15
    assert abs(snap.mean_speed - (12.0 / 3.0)) < 0.01
    assert len(snap.samples) == 2
    assert any("DADOS ATIVOS" in event for event in snap.recent_events)

def test_record_traffic_frame_all_zeros():
    telemetry = TelemetryState()

    edges = {
        "e1": MockEdgeState(0.0, 0.0, 0, 0.0),
        "e2": MockEdgeState(0.0, 0.0, 0, 0.0),
    }

    telemetry.record_traffic_frame(sequence_id=1, timestamp=1.0, edges_dict=edges)
    snap = telemetry.get_snapshot()

    assert snap.all_zeros is True
    assert snap.active_edges_count == 0
    assert snap.max_occupancy == 0.0
    assert len(snap.samples) == 2
    assert any("DADOS ZERADOS" in event for event in snap.recent_events)

def test_frame_rate_calculation(monkeypatch):
    telemetry = TelemetryState()
    current_time = 1000.0

    def mock_time():
        nonlocal current_time
        return current_time

    monkeypatch.setattr(time, "time", mock_time)

    edges = {"e1": MockEdgeState(occupancy=0.1)}
    # Send 11 frames spaced by 0.1s (10 Hz)
    for i in range(1, 12):
        current_time += 0.1
        telemetry.record_traffic_frame(sequence_id=i, timestamp=float(i), edges_dict=edges)

    snap = telemetry.get_snapshot()
    # 10 intervals of 0.1s = 1.0s total -> 10 frames / 1.0s = 10.0 Hz
    assert abs(snap.frame_rate_hz - 10.0) < 0.2

def test_frame_milestone_event():
    telemetry = TelemetryState()
    edges = {"e1": MockEdgeState(0.1, 10.0, 1, 0.1)}
    telemetry._total_frames = 499  # Simulate reaching frame 499
    telemetry.record_traffic_frame(sequence_id=500, timestamp=50.0, edges_dict=edges)

    snap = telemetry.get_snapshot()
    assert any("Frame #500 recebido" in event for event in snap.recent_events)

def test_max_events_buffer():
    max_ev = 5
    telemetry = TelemetryState(max_events=max_ev)
    for i in range(20):
        telemetry.record_event(f"Evento {i}")

    snap = telemetry.get_snapshot()
    assert len(snap.recent_events) == max_ev
    assert "Evento 19" in snap.recent_events[-1]

def test_connection_timeout(monkeypatch):
    telemetry = TelemetryState()
    current_time = 100.0
    monkeypatch.setattr(time, "time", lambda: current_time)

    telemetry.record_ping()
    assert telemetry.get_snapshot().connected is True

    # Advance 6 seconds with no activity -> timeout
    current_time += 6.0
    assert telemetry.get_snapshot().connected is False

def test_concurrent_access():
    telemetry = TelemetryState()
    edges = {"e1": MockEdgeState(0.5, 10.0, 1, 0.2)}
    stop_event = threading.Event()

    def writer_thread(tid):
        for i in range(100):
            telemetry.record_traffic_frame(sequence_id=i + 1, timestamp=float(i), edges_dict=edges)
            telemetry.record_ping()
            telemetry.record_event(f"T{tid} msg {i}")

    def reader_thread():
        while not stop_event.is_set():
            snap = telemetry.get_snapshot()
            assert snap.total_frames >= 0

    threads = [threading.Thread(target=writer_thread, args=(i,)) for i in range(5)]
    reader = threading.Thread(target=reader_thread)

    reader.start()
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    stop_event.set()
    reader.join()

    snap = telemetry.get_snapshot()
    assert snap.total_frames > 0
