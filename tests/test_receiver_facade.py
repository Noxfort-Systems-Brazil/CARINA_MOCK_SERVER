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
# File: tests/test_receiver_facade.py
# Author: Gabriel Moraes
# Date: October 2026

from unittest.mock import MagicMock, patch
from src.receiver_facade import ReceiverFacade
from src.core.config import Config
from src.core.telemetry_state import TelemetryState
from tests.conftest import InMemoryLogger

def test_receiver_facade_init_and_setup():
    logger = InMemoryLogger()
    config = Config()
    config.port = 54322
    telemetry = TelemetryState()
    mock_storage = MagicMock()
    mock_parser = MagicMock()

    facade = ReceiverFacade(
        config=config,
        logger=logger,
        telemetry=telemetry,
        map_storage=mock_storage,
        map_parser=mock_parser
    )

    assert facade.grpc_server is None
    assert facade.hft_service is None

    facade.setup()

    assert facade.hft_service is not None
    assert facade.grpc_server is not None
    assert any("Configurando subsistemas" in log[1] for log in logger.logs)

def test_receiver_facade_run_headless(monkeypatch):
    logger = InMemoryLogger()
    config = Config()
    config.port = 54323
    facade = ReceiverFacade(config=config, logger=logger)

    facade.setup()
    facade.grpc_server.start = MagicMock()
    facade.grpc_server.wait_for_termination = MagicMock()
    facade.grpc_server.stop = MagicMock()

    facade.run(headless=True)

    assert facade._is_running is True
    facade.grpc_server.start.assert_called_once()
    facade.grpc_server.wait_for_termination.assert_called_once()

    facade.stop()
    assert facade._is_running is False
    facade.grpc_server.stop.assert_called_once()

def test_receiver_facade_stop_idempotent():
    logger = InMemoryLogger()
    facade = ReceiverFacade(logger=logger)
    # Stop before running should not fail
    facade.stop()
    assert facade._is_running is False

def test_receiver_facade_fallback_to_headless_when_gui_fails():
    logger = InMemoryLogger()
    facade = ReceiverFacade(logger=logger)
    facade.setup()

    facade.grpc_server.start = MagicMock()
    facade.grpc_server.wait_for_termination = MagicMock()

    # Simulate failure when opening Tkinter (common on headless servers)
    with patch("src.receiver_facade.TkinterDashboard", side_effect=RuntimeError("No X11 display")):
        facade.run(headless=False)

    assert any("Alternando para modo headless" in log[1] for log in logger.logs)
    facade.grpc_server.wait_for_termination.assert_called_once()
    facade.stop()
