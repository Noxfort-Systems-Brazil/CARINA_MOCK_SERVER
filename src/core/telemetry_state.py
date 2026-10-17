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
# File: src/core/telemetry_state.py
# Author: Gabriel Moraes
# Date: October 2026

import time
import threading
from collections import deque
from typing import Any, Dict, List, Optional
from src.core.interfaces import (
    ITelemetryCollector,
    ITelemetryProvider,
    TelemetrySnapshot,
    EdgeSample
)

class TelemetryState(ITelemetryCollector, ITelemetryProvider):
    """
    Thread-safe implementation of Telemetry Collector and Provider.
    Calculates zero-value diagnostics, network throughput (Hz), and maintains
    a limited event buffer.
    """
    def __init__(self, max_events: int = 15):
        self._lock = threading.Lock()
        
        # Connection status
        self._connected = False
        self._server_state = "IDLE"
        self._last_ping_time: Optional[float] = None
        
        # Scenario metadata
        self._scenario_loaded = False
        self._map_name = "Nenhum"
        self._map_hash = ""
        self._nodes_count = 0
        self._edges_count = 0
        self._file_size_bytes = 0
        
        # Traffic stream metrics
        self._total_frames = 0
        self._last_sequence_id = 0
        self._last_timestamp = 0.0
        self._last_frame_received_wall_time: Optional[float] = None
        
        # Frame rate calculation (sliding window)
        self._frame_times = deque(maxlen=20)
        self._frame_rate_hz = 0.0
        
        # Zero-value detection & edge metrics
        self._all_zeros = True
        self._total_edges_in_frame = 0
        self._active_edges_count = 0
        self._max_occupancy = 0.0
        self._mean_speed = 0.0
        self._max_queue = 0
        self._samples: List[EdgeSample] = []
        
        # Recent events buffer
        self._recent_events = deque(maxlen=max_events)
        self._add_event("Servidor inicializado. Aguardando Synapse...")

    def _add_event(self, message: str) -> None:
        timestamp_str = time.strftime('%H:%M:%S')
        self._recent_events.append(f"[{timestamp_str}] {message}")

    def record_ping(self) -> None:
        with self._lock:
            now = time.time()
            self._connected = True
            self._last_ping_time = now
            self._add_event("Ping recebido do Synapse")

    def record_scenario(self, map_hash: str, map_name: str, file_size: int, nodes: int, edges: int) -> None:
        with self._lock:
            self._connected = True
            self._scenario_loaded = True
            self._map_hash = map_hash
            self._map_name = map_name if map_name else "cenario.net.xml"
            self._file_size_bytes = file_size
            self._nodes_count = nodes
            self._edges_count = edges
            self._server_state = "READY"
            size_kb = file_size / 1024
            self._add_event(f"Cenário carregado: {self._map_name} ({nodes} nós, {edges} arestas, {size_kb:.1f} KB)")

    def record_control(self, action_name: str, new_state: str) -> None:
        with self._lock:
            self._connected = True
            self._server_state = new_state
            self._add_event(f"Comando: {action_name} -> Estado: {new_state}")

    def record_traffic_frame(self, sequence_id: int, timestamp: float, edges_dict: Dict[str, Any]) -> None:
        with self._lock:
            now = time.time()
            self._connected = True
            
            # Update frame rate (Hz)
            self._frame_times.append(now)
            if len(self._frame_times) > 1:
                duration = self._frame_times[-1] - self._frame_times[0]
                if duration > 0:
                    self._frame_rate_hz = (len(self._frame_times) - 1) / duration
                else:
                    self._frame_rate_hz = 0.0
            
            self._last_frame_received_wall_time = now

            # If heartbeat (sequence_id 0 or empty edges), update connection and frame rate only
            if sequence_id == 0 or len(edges_dict) == 0:
                return

            self._total_frames += 1
            self._last_sequence_id = sequence_id
            self._last_timestamp = timestamp
            
            # --- ZERO VALUE & ACTIVE DATA DIAGNOSTICS ---
            total_edges = len(edges_dict)
            self._total_edges_in_frame = total_edges
            
            active_count = 0
            max_occ = 0.0
            sum_speed = 0.0
            max_q = 0
            
            active_samples: List[EdgeSample] = []
            zero_samples: List[EdgeSample] = []
            
            for edge_id, state in edges_dict.items():
                occ = float(getattr(state, "occupancy", 0.0))
                speed = float(getattr(state, "mean_speed", 0.0))
                queue = int(getattr(state, "queue_length", 0))
                density = float(getattr(state, "density", 0.0))
                
                # Check if this edge has any non-zero value
                is_active = (occ > 0.0001) or (speed > 0.0001) or (queue > 0) or (density > 0.0001)
                
                sample = EdgeSample(
                    edge_id=edge_id,
                    occupancy=occ,
                    mean_speed=speed,
                    queue_length=queue,
                    density=density
                )
                
                if is_active:
                    active_count += 1
                    if len(active_samples) < 5:
                        active_samples.append(sample)
                else:
                    if len(zero_samples) < 3:
                        zero_samples.append(sample)
                
                if occ > max_occ:
                    max_occ = occ
                if queue > max_q:
                    max_q = queue
                sum_speed += speed

            self._active_edges_count = active_count
            self._max_occupancy = max_occ
            self._max_queue = max_q
            self._mean_speed = (sum_speed / total_edges) if total_edges > 0 else 0.0
            
            # If no active edges, all values in this frame are zeros
            self._all_zeros = (active_count == 0)
            
            # Prioritize showing active samples; fallback to zero samples
            self._samples = active_samples if active_samples else zero_samples
            
            # Periodic event log for frame progression
            if self._total_frames == 1:
                diag_msg = "Frame 1 recebido: " + ("⚠️ DADOS ZERADOS" if self._all_zeros else f"🟢 DADOS ATIVOS ({active_count}/{total_edges} arestas)")
                self._add_event(diag_msg)
            elif self._total_frames % 500 == 0:
                self._add_event(f"Frame #{self._total_frames} recebido ({self._frame_rate_hz:.1f} Hz)")

    def record_event(self, message: str) -> None:
        with self._lock:
            self._add_event(message)

    def get_snapshot(self) -> TelemetrySnapshot:
        with self._lock:
            now = time.time()
            time_since_ping = (now - self._last_ping_time) if self._last_ping_time else None
            time_since_frame = (now - self._last_frame_received_wall_time) if self._last_frame_received_wall_time else None
            
            # Check connection timeout (if no frame or ping in last 5 seconds, mark inactive)
            is_active_connection = self._connected
            if self._last_ping_time or self._last_frame_received_wall_time:
                last_activity = max(
                    self._last_ping_time or 0.0,
                    self._last_frame_received_wall_time or 0.0
                )
                if now - last_activity > 5.0:
                    is_active_connection = False
            
            return TelemetrySnapshot(
                connected=is_active_connection,
                server_state=self._server_state,
                last_ping_time=self._last_ping_time,
                time_since_last_ping=time_since_ping,
                scenario_loaded=self._scenario_loaded,
                map_name=self._map_name,
                map_hash=self._map_hash,
                nodes_count=self._nodes_count,
                edges_count=self._edges_count,
                file_size_bytes=self._file_size_bytes,
                total_frames=self._total_frames,
                last_sequence_id=self._last_sequence_id,
                last_timestamp=self._last_timestamp,
                frame_rate_hz=self._frame_rate_hz,
                time_since_last_frame=time_since_frame,
                all_zeros=self._all_zeros,
                total_edges_in_frame=self._total_edges_in_frame,
                active_edges_count=self._active_edges_count,
                max_occupancy=self._max_occupancy,
                mean_speed=self._mean_speed,
                max_queue=self._max_queue,
                samples=list(self._samples),
                recent_events=list(self._recent_events)
            )
