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
# File: src/core/interfaces.py
# Author: Gabriel Moraes
# Date: 2026-09-29

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

class ILogger(ABC):
    @abstractmethod
    def info(self, message: str, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def warning(self, message: str, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def error(self, message: str, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def debug(self, message: str, **kwargs: Any) -> None:
        pass


@dataclass
class EdgeSample:
    edge_id: str
    occupancy: float
    mean_speed: float
    queue_length: int
    density: float


@dataclass
class TelemetrySnapshot:
    # Connection status
    connected: bool
    server_state: str
    last_ping_time: Optional[float]
    time_since_last_ping: Optional[float]
    
    # Scenario
    scenario_loaded: bool
    map_name: str
    map_hash: str
    nodes_count: int
    edges_count: int
    file_size_bytes: int
    
    # Telemetry & Traffic Diagnostics
    total_frames: int
    last_sequence_id: int
    last_timestamp: float
    frame_rate_hz: float
    time_since_last_frame: Optional[float]
    
    # Zero-Value Data Detection
    all_zeros: bool
    total_edges_in_frame: int
    active_edges_count: int
    max_occupancy: float
    mean_speed: float
    max_queue: int
    samples: List[EdgeSample]
    
    # Recent Events Log
    recent_events: List[str]


class ITelemetryCollector(ABC):
    """Interface for recording telemetry events and metrics."""
    @abstractmethod
    def record_ping(self) -> None:
        pass

    @abstractmethod
    def record_scenario(self, map_hash: str, map_name: str, file_size: int, nodes: int, edges: int) -> None:
        pass

    @abstractmethod
    def record_control(self, action_name: str, new_state: str) -> None:
        pass

    @abstractmethod
    def record_traffic_frame(self, sequence_id: int, timestamp: float, edges_dict: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def record_event(self, message: str) -> None:
        pass


class ITelemetryProvider(ABC):
    """Read-only interface for telemetry snapshot queries by the UI."""
    @abstractmethod
    def get_snapshot(self) -> TelemetrySnapshot:
        pass


class IUserInterface(ABC):
    """Interface defining the lifecycle contract for any UI."""
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class IMapParser(ABC):
    """Interface for parsing and extracting topology and traffic lights from map files (e.g., SUMO .net.xml)."""
    @abstractmethod
    def parse_net_xml(self, file_path: str) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Return (shapes, traffic_lights) extracted from the map.
        """
        pass


class IMapStorage(ABC):
    """Interface for managing and persisting received map files."""
    @abstractmethod
    def save_map(self, map_name: str, content: bytes) -> str:
        """
        Save binary map content to disk and return the absolute path of the saved file.
        """
        pass

    @abstractmethod
    def get_map_path(self, map_name: str) -> Optional[str]:
        """
        Return the file path if it exists.
        """
        pass


class IGrpcServer(ABC):
    """Interface for gRPC server lifecycle control."""
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self, grace_period: float = 0.0) -> None:
        pass

    @abstractmethod
    def wait_for_termination(self) -> None:
        pass


class IReceiverFacade(ABC):
    """Interface for the main Mock Server Orchestrator / Facade."""
    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def run(self, headless: bool = False) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

