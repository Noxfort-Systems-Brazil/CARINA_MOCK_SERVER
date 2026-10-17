# CARINA Mock Server - High-Frequency Telemetry & Synapse Protocol Test Harness
# SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File: tests/test_hft_service.py
# Author: Gabriel Moraes
# Date: October 2026

from unittest.mock import MagicMock
import synapse_hft_pb2 as pb2
from src.application.hft_service import HFTService
from tests.conftest import InMemoryLogger

def test_hft_service_ping(telemetry_state):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)

    context = MagicMock()
    response = service.Ping(pb2.Empty(), context)

    assert response.active is True
    assert response.state == "IDLE"
    assert response.server_time > 0
    assert telemetry_state.get_snapshot().connected is True

def test_hft_service_load_scenario_with_map(telemetry_state):
    logger = InMemoryLogger()
    mock_storage = MagicMock()
    mock_storage.save_map.return_value = "/tmp/saved_map.net.xml"

    mock_parser = MagicMock()
    mock_parser.parse_net_xml.return_value = ([{"id": "lane_1"}], [{"id": "tl_1"}])

    service = HFTService(
        logger=logger,
        telemetry=telemetry_state,
        map_storage=mock_storage,
        map_parser=mock_parser
    )

    request = pb2.ScenarioDefinition()
    request.map_hash = "abc123hash"
    request.map_file_name = "test_map.net.xml"
    request.map_file_content = b"<net>binary_xml</net>"

    context = MagicMock()
    response = service.LoadScenario(request, context)

    assert response.accepted is True
    assert "Map Saved" in response.message
    assert "Parsed 1 lanes, 1 TLs" in response.message

    mock_storage.save_map.assert_called_once_with("test_map.net.xml", b"<net>binary_xml</net>")
    mock_parser.parse_net_xml.assert_called_once_with("/tmp/saved_map.net.xml")

    snap = telemetry_state.get_snapshot()
    assert snap.scenario_loaded is True
    assert snap.map_hash == "abc123hash"

def test_hft_service_load_scenario_storage_error(telemetry_state):
    logger = InMemoryLogger()
    mock_storage = MagicMock()
    mock_storage.save_map.side_effect = IOError("Disk full")

    service = HFTService(
        logger=logger,
        telemetry=telemetry_state,
        map_storage=mock_storage
    )

    request = pb2.ScenarioDefinition()
    request.map_file_content = b"content"

    context = MagicMock()
    response = service.LoadScenario(request, context)

    assert response.accepted is True
    assert "Storage/Parser Warning" in response.message

def test_hft_service_system_control(telemetry_state):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)

    context = MagicMock()

    # START command
    cmd_start = pb2.ControlCommand(action=pb2.ControlCommand.START)
    resp_start = service.SystemControl(cmd_start, context)
    assert resp_start.success is True
    assert resp_start.new_state == "RUNNING"
    assert service.state == "RUNNING"

    # STOP command
    cmd_stop = pb2.ControlCommand(action=pb2.ControlCommand.STOP)
    resp_stop = service.SystemControl(cmd_stop, context)
    assert resp_stop.success is True
    assert resp_stop.new_state == "IDLE"
    assert service.state == "IDLE"

def test_hft_service_stream_traffic(telemetry_state, sample_traffic_frame):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)
    service.state = "RUNNING"

    # Simulate frame stream
    frames = [sample_traffic_frame, sample_traffic_frame]
    context = MagicMock()

    response = service.StreamTraffic(iter(frames), context)

    assert response.active is True
    assert response.state == "RUNNING"

    snap = telemetry_state.get_snapshot()
    assert snap.total_frames == 2
    assert snap.last_sequence_id == sample_traffic_frame.sequence_id

def test_hft_service_stream_traffic_cancelled(telemetry_state, sample_traffic_frame):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)
    service.state = "RUNNING"

    def frame_generator():
        yield sample_traffic_frame
        raise Exception("Stream Cancelled")

    context = MagicMock()
    response = service.StreamTraffic(frame_generator(), context)

    assert response.active is True
    assert any("cancelled" in log[1].lower() for log in logger.logs)

def test_hft_service_stream_traffic_error(telemetry_state, sample_traffic_frame):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)
    service.state = "RUNNING"

    def frame_generator():
        yield sample_traffic_frame
        raise RuntimeError("Fatal deserialization error")

    context = MagicMock()
    response = service.StreamTraffic(frame_generator(), context)

    assert response.active is True
    assert any(log[0] == "ERROR" and "Stream ended with error" in log[1] for log in logger.logs)
