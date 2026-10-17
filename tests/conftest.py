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
# File: tests/conftest.py
# Author: Gabriel Moraes
# Date: October 2026

import sys
import os
import pytest
from unittest.mock import MagicMock

# Ensure local and proto imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../proto")))

import synapse_hft_pb2 as pb2
from src.core.interfaces import ILogger
from src.core.telemetry_state import TelemetryState


class InMemoryLogger(ILogger):
    """In-memory logger for test assertion verification."""
    def __init__(self):
        self.logs = []

    def info(self, message: str, **kwargs) -> None:
        self.logs.append(("INFO", message, kwargs))

    def warning(self, message: str, **kwargs) -> None:
        self.logs.append(("WARNING", message, kwargs))

    def error(self, message: str, **kwargs) -> None:
        self.logs.append(("ERROR", message, kwargs))

    def debug(self, message: str, **kwargs) -> None:
        self.logs.append(("DEBUG", message, kwargs))


@pytest.fixture
def memory_logger():
    return InMemoryLogger()


@pytest.fixture
def mock_logger():
    return MagicMock(spec=ILogger)


@pytest.fixture
def telemetry_state():
    return TelemetryState(max_events=10)


@pytest.fixture
def sample_traffic_frame():
    frame = pb2.TrafficFrame()
    frame.sequence_id = 42
    frame.timestamp = 100.5

    edge1 = frame.edges["edge_alpha"]
    edge1.occupancy = 0.85
    edge1.mean_speed = 5.2
    edge1.queue_length = 12
    edge1.density = 0.7

    edge2 = frame.edges["edge_beta"]
    edge2.occupancy = 0.30
    edge2.mean_speed = 14.5
    edge2.queue_length = 2
    edge2.density = 0.2

    return frame
