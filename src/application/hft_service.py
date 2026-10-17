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
# File: src/application/hft_service.py
# Author: Gabriel Moraes
# Date: October 2026

import time
import grpc
from typing import Iterator, Optional

# Import proto definitions
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../proto")))

import synapse_hft_pb2 as pb2
import synapse_hft_pb2_grpc as pb2_grpc
from src.core.interfaces import ILogger, ITelemetryCollector, IMapStorage, IMapParser

class HFTService(pb2_grpc.HFTLinkServicer):
    def __init__(
        self,
        logger: ILogger,
        telemetry: Optional[ITelemetryCollector] = None,
        map_storage: Optional[IMapStorage] = None,
        map_parser: Optional[IMapParser] = None
    ):
        self._logger = logger
        self._telemetry = telemetry
        self._map_storage = map_storage
        self._map_parser = map_parser
        self.state = "IDLE"
        self._logger.info("HFTService initialized.")

    def Ping(self, request: pb2.Empty, context: grpc.ServicerContext) -> pb2.SystemState:
        self._logger.info("Received Ping request.")
        if self._telemetry:
            self._telemetry.record_ping()
            
        return pb2.SystemState(
            active=True,
            state=self.state,
            server_time=int(time.time() * 1000)
        )

    def LoadScenario(self, request: pb2.ScenarioDefinition, context: grpc.ServicerContext) -> pb2.ScenarioStatus:
        file_size = len(request.map_file_content) if request.map_file_content else 0
        nodes_count = len(request.graph.nodes) if request.HasField("graph") else 0
        edges_count = len(request.graph.edges) if request.HasField("graph") else 0
        map_name = request.map_file_name if request.map_file_name else "scenario.net.xml"

        self._logger.info(
            "Received LoadScenario.",
            map_hash=request.map_hash,
            map_file_name=map_name,
            file_size_bytes=file_size,
            nodes=nodes_count,
            edges=edges_count
        )

        status_messages = []
        # Decoupled processing of map file if present
        if request.map_file_content and self._map_storage:
            try:
                saved_path = self._map_storage.save_map(map_name, request.map_file_content)
                status_messages.append("Map Saved")

                if self._map_parser:
                    shapes, tls = self._map_parser.parse_net_xml(saved_path)
                    if shapes or tls:
                        status_messages.append(f"Parsed {len(shapes)} lanes, {len(tls)} TLs")
            except Exception as e:
                self._logger.error(f"Erro ao processar conteúdo do mapa: {e}")
                status_messages.append(f"Storage/Parser Warning: {e}")

        if self._telemetry:
            self._telemetry.record_scenario(
                map_hash=request.map_hash,
                map_name=map_name,
                file_size=file_size,
                nodes=nodes_count,
                edges=edges_count
            )

        msg = "Scenario successfully loaded and validated by Mock Server."
        if status_messages:
            msg += f" ({', '.join(status_messages)})"

        return pb2.ScenarioStatus(
            accepted=True,
            message=msg
        )

    def SystemControl(self, request: pb2.ControlCommand, context: grpc.ServicerContext) -> pb2.CommandResponse:
        cmd = request.action
        cmd_name = pb2.ControlCommand.Action.Name(cmd)
        self._logger.info(f"🎮 COMMAND: {cmd_name}")
        
        if cmd == pb2.ControlCommand.START:
            self.state = "RUNNING"
            self._logger.info("   └── SYSTEM STARTED.")
        elif cmd == pb2.ControlCommand.STOP:
            self.state = "IDLE"
            self._logger.info("   └── SYSTEM STOPPED.")

        if self._telemetry:
            self._telemetry.record_control(cmd_name, self.state)
            
        return pb2.CommandResponse(success=True, new_state=self.state)

    def StreamTraffic(self, request_iterator: Iterator[pb2.TrafficFrame], context: grpc.ServicerContext) -> pb2.SystemState:
        if self.state != "RUNNING":
             self._logger.warning("⚠️  Stream ignored (Not RUNNING).")
        
        self._logger.info("🌊 INCOMING TRAFFIC STREAM...")
        try:
            for frame in request_iterator:
                # Update telemetry state and zero-value diagnostic
                if self._telemetry:
                    self._telemetry.record_traffic_frame(
                        sequence_id=frame.sequence_id,
                        timestamp=frame.timestamp,
                        edges_dict=dict(frame.edges)
                    )

                # --- DETAILED PACKET LOG VIEW ---
                self._logger.info(f"📦 FRAME SEQ: {frame.sequence_id} | Timestamp: {frame.timestamp:.2f}")
                
                count = 0
                for edge_id, state in frame.edges.items():
                    # Show first 5 in the log for inspection
                    if count < 5:
                        status_icon = "🟢"  # Free flow
                        if state.occupancy > 0.8:
                            status_icon = "🔴"  # Congested
                        elif state.occupancy > 0.4:
                            status_icon = "🟡"  # Heavy
                        
                        self._logger.info(f"   ├── {status_icon} Edge: {edge_id}")
                        self._logger.info(f"   │   ├── Ocupação: {state.occupancy*100:.1f}%")
                        self._logger.info(f"   │   ├── Velocidade Média: {state.mean_speed:.2f} m/s")
                        self._logger.info(f"   │   └── Veículos na Fila: {state.queue_length}")
                        count += 1
                
                if len(frame.edges) > 5:
                    self._logger.info(f"   └── ... e mais {len(frame.edges)-5} arestas neste pacote.")
                self._logger.info("   └───────────────────────────────────────────────────")
                
        except Exception as e:
            err_msg = str(e)
            if "Cancelled" in err_msg or err_msg == "":
                self._logger.info("StreamTraffic cancelled by client or stopped gracefully.")
            else:
                self._logger.error(f"❌ Stream ended with error: {err_msg}")
            
        return pb2.SystemState(
            active=True,
            state=self.state,
            server_time=int(time.time() * 1000)
        )
