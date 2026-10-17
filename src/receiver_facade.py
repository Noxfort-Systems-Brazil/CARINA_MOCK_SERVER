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
# File: src/receiver_facade.py
# Author: Gabriel Moraes
# Date: October 2026

import sys
import os
import signal
from typing import Optional

from src.core.interfaces import (
    IReceiverFacade,
    ILogger,
    IMapStorage,
    IMapParser,
    IGrpcServer,
    IUserInterface
)
from src.core.config import Config
from src.core.telemetry_state import TelemetryState
from src.infrastructure.console_logger import ConsoleLogger
from src.infrastructure.file_logger import FileLogger
from src.infrastructure.composite_logger import CompositeLogger
from src.infrastructure.map_storage import LocalMapStorage
from src.infrastructure.sumo_parser import SumoNetParser
from src.infrastructure.grpc_server import GrpcServer
from src.application.hft_service import HFTService
from ui.dashboard import TkinterDashboard


class ReceiverFacade(IReceiverFacade):
    """
    Pure Facade and Orchestrator for the CARINA Mock Server.
    
    Responsibilities:
    - Instantiate and orchestrate the lifecycle of all infrastructure modules,
      application services, persistence, and graphical interface.
    - Centralize graceful shutdown control and system signal handling.
    - Maintain zero business logic coupling, acting as the single coordination point.
    """
    def __init__(
        self,
        config: Optional[Config] = None,
        logger: Optional[ILogger] = None,
        telemetry: Optional[TelemetryState] = None,
        map_storage: Optional[IMapStorage] = None,
        map_parser: Optional[IMapParser] = None,
    ):
        self.config = config or Config()
        self.logger = logger or CompositeLogger([
            ConsoleLogger(),
            FileLogger("mock_server.log")
        ])
        self.telemetry = telemetry or TelemetryState()
        self.map_storage = map_storage or LocalMapStorage(storage_dir="data/maps", logger=self.logger)
        self.map_parser = map_parser or SumoNetParser(logger=self.logger)
        
        self.hft_service: Optional[HFTService] = None
        self.grpc_server: Optional[IGrpcServer] = None
        self.dashboard: Optional[IUserInterface] = None
        self._is_running = False

    def setup(self) -> None:
        """Initialize services and prepare gRPC connections and listeners."""
        self.logger.info("Configurando subsistemas do Mock Server...")
        
        self.hft_service = HFTService(
            logger=self.logger,
            telemetry=self.telemetry,
            map_storage=self.map_storage,
            map_parser=self.map_parser
        )
        
        self.grpc_server = GrpcServer(
            servicer=self.hft_service,
            address=self.config.server_address,
            logger=self.logger
        )

        # Register OS termination signals
        def _signal_handler(*_):
            self.logger.info("Sinal de interrupção recebido.")
            self.stop()
            sys.exit(0)

        try:
            signal.signal(signal.SIGINT, _signal_handler)
            signal.signal(signal.SIGTERM, _signal_handler)
        except (ValueError, AttributeError):
            # Can occur if not in the main thread
            pass

    def run(self, headless: bool = False) -> None:
        """
        Start gRPC server and run UI or wait in headless mode.
        """
        if not self.grpc_server:
            self.setup()

        self._is_running = True
        self.logger.info("Iniciando CARINA Mock Server Facade", address=self.config.server_address)
        self.grpc_server.start()

        is_headless = headless or os.getenv("MOCK_SERVER_NO_GUI") == "1"

        if is_headless:
            self.logger.info("Executando em modo headless (--no-gui). Pressione Ctrl+C para encerrar.")
            try:
                self.grpc_server.wait_for_termination()
            except KeyboardInterrupt:
                self.stop()
            else:
                pass
        else:
            try:
                self.logger.info("Iniciando Dashboard Gráfico...")
                self.dashboard = TkinterDashboard(
                    telemetry_provider=self.telemetry,
                    on_close=self.stop
                )
                self.dashboard.start()
            except Exception as e:
                self.logger.error(f"Não foi possível abrir a interface gráfica ({e}). Alternando para modo headless.")
                try:
                    self.grpc_server.wait_for_termination()
                except KeyboardInterrupt:
                    self.stop()

    def stop(self) -> None:
        """Gracefully shut down all active services, threads, and interfaces."""
        if not self._is_running:
            return

        self._is_running = False
        self.logger.info("Desligando CARINA Mock Server...")
        
        if self.grpc_server:
            self.grpc_server.stop(grace_period=0.0)
            
        if self.dashboard:
            try:
                self.dashboard.stop()
            except Exception:
                pass

        self.logger.info("Todos os serviços foram finalizados com sucesso.")
