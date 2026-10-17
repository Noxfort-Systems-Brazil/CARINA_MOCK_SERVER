# CARINA Mock Server - High-Frequency Telemetry & Synapse Protocol Test Harness
# Copyright (C) 2026 Noxfort Systems
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
# File: src/infrastructure/grpc_server.py
# Author: Gabriel Moraes
# Date: October 2026

from concurrent import futures
from typing import Optional
import grpc

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../proto")))
import synapse_hft_pb2_grpc as pb2_grpc

from src.core.interfaces import IGrpcServer, ILogger

class GrpcServer(IGrpcServer):
    """
    Encapsulates the gRPC server for the CARINA Mock HFTLink service.
    Configures payload limits (50MB to support complex maps),
    thread pool, and lifecycle (start, stop, wait_for_termination).
    """
    def __init__(
        self,
        servicer: pb2_grpc.HFTLinkServicer,
        address: str = "0.0.0.0:50051",
        max_workers: int = 10,
        max_message_length: int = 50 * 1024 * 1024,
        logger: Optional[ILogger] = None
    ):
        self._servicer = servicer
        self._address = address
        self._max_workers = max_workers
        self._max_message_length = max_message_length
        self._logger = logger
        self._server: Optional[grpc.Server] = None
        self._is_running = False

    def start(self) -> None:
        if self._is_running:
            return

        self._server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=self._max_workers),
            options=[
                ('grpc.max_receive_message_length', self._max_message_length),
                ('grpc.max_send_message_length', self._max_message_length),
            ]
        )
        pb2_grpc.add_HFTLinkServicer_to_server(self._servicer, self._server)
        self._server.add_insecure_port(self._address)
        
        if self._logger:
            self._logger.info("Iniciando servidor gRPC", address=self._address, max_payload_mb=self._max_message_length // (1024 * 1024))
            
        self._server.start()
        self._is_running = True

    def stop(self, grace_period: float = 0.0) -> None:
        if not self._is_running or self._server is None:
            return

        if self._logger:
            self._logger.info("Encerrando servidor gRPC...", grace_period=grace_period)

        self._server.stop(grace_period)
        self._is_running = False
        if self._logger:
            self._logger.info("Servidor gRPC encerrado com sucesso.")

    def wait_for_termination(self) -> None:
        if self._server and self._is_running:
            self._server.wait_for_termination()
