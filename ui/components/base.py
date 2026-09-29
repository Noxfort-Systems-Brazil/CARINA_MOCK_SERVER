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
# File: ui/components/base.py
# Author: Gabriel Moraes
# Date: 2026-09-29

from abc import ABC, abstractmethod
import tkinter as tk
from src.core.interfaces import TelemetrySnapshot

class IDashboardComponent(ABC):
    """
    Base contract for visual dashboard components.
    Each component is responsible for building its layout and updating its state
    from a TelemetrySnapshot.
    """

    @abstractmethod
    def build(self, parent: tk.Misc) -> tk.Widget:
        """Build component widgets and return the main container."""
        pass

    @abstractmethod
    def update(self, snapshot: TelemetrySnapshot) -> None:
        """Update visual elements of the component with snapshot data."""
        pass
