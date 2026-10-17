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
# File: ui/dashboard.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional

from src.core.interfaces import IUserInterface, ITelemetryProvider, TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent
from ui.components.header import HeaderComponent
from ui.components.connection_card import ConnectionCardComponent
from ui.components.scenario_card import ScenarioCardComponent
from ui.components.diagnostics_card import DiagnosticsCardComponent
from ui.components.stream_card import StreamCardComponent
from ui.components.events_card import EventsCardComponent

class TkinterDashboard(IUserInterface):
    """
    Modern Dark Mode Tkinter Dashboard for Carina Mock Server.
    Acts as Orchestrator: manages main window, global styles, lifecycle,
    periodic telemetry polling, and delegates rendering to modular subcomponents.
    """
    def __init__(self, telemetry_provider: ITelemetryProvider, on_close: Optional[Callable[[], None]] = None):
        self._provider = telemetry_provider
        self._on_close = on_close
        self._is_running = False
        self._components: List[IDashboardComponent] = []
        
        # Build UI
        self._root = tk.Tk()
        self._root.title("CARINA Mock Server - Telemetria & Diagnóstico Synapse")
        self._root.geometry("860x720")
        self._root.minsize(780, 640)
        self._root.configure(bg=Theme.BG_MAIN)
        
        self._root.protocol("WM_DELETE_WINDOW", self._handle_close)
        
        self._setup_styles()
        self._build_layout()

    def _setup_styles(self) -> None:
        style = ttk.Style(self._root)
        style.theme_use("clam")
        
        # Configure general Treeview style
        style.configure(
            "Treeview",
            background=Theme.BG_CARD,
            foreground=Theme.TEXT_MAIN,
            fieldbackground=Theme.BG_CARD,
            rowheight=22,
            font=Theme.FONT_MONO_SM,
            borderwidth=0
        )
        style.configure(
            "Treeview.Heading",
            background=Theme.BG_CARD_ALT,
            foreground=Theme.TEXT_MUTED,
            font=Theme.FONT_SECTION_HEADER,
            relief="flat"
        )
        style.map("Treeview", background=[("selected", Theme.BG_ACCENT_HOVER)])

    def _build_layout(self) -> None:
        main_frame = tk.Frame(self._root, bg=Theme.BG_MAIN, padx=16, pady=12)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Header Bar
        header = HeaderComponent()
        header_widget = header.build(main_frame)
        header_widget.pack(fill=tk.X, pady=(0, 10))
        self._components.append(header)

        # 2. Status & Scenario (2 Columns)
        top_row = tk.Frame(main_frame, bg=Theme.BG_MAIN)
        top_row.pack(fill=tk.X, pady=(0, 10))
        top_row.columnconfigure(0, weight=1, uniform="top_cards")
        top_row.columnconfigure(1, weight=1, uniform="top_cards")

        conn_card = ConnectionCardComponent()
        conn_widget = conn_card.build(top_row)
        conn_widget.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        self._components.append(conn_card)

        scenario_card = ScenarioCardComponent()
        scenario_widget = scenario_card.build(top_row)
        scenario_widget.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        self._components.append(scenario_card)

        # 3. Central Diagnostics Card
        diag_card = DiagnosticsCardComponent()
        diag_widget = diag_card.build(main_frame)
        diag_widget.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self._components.append(diag_card)

        # 4. Stream & Recent Events (2 Columns)
        bottom_row = tk.Frame(main_frame, bg=Theme.BG_MAIN)
        bottom_row.pack(fill=tk.X)
        bottom_row.columnconfigure(0, weight=1, uniform="bottom_cards")
        bottom_row.columnconfigure(1, weight=2, uniform="bottom_cards")

        stream_card = StreamCardComponent()
        stream_widget = stream_card.build(bottom_row)
        stream_widget.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        self._components.append(stream_card)

        events_card = EventsCardComponent()
        events_widget = events_card.build(bottom_row)
        events_widget.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        self._components.append(events_card)

    def _refresh_ui(self) -> None:
        """Fetches telemetry snapshot and delegates update to all registered components."""
        if not self._is_running:
            return

        try:
            snap: TelemetrySnapshot = self._provider.get_snapshot()
            for component in self._components:
                component.update(snap)
        except Exception:
            # Prevent crashes during UI update
            pass

        # Schedule next update in 100ms (10 FPS)
        if self._is_running:
            self._root.after(100, self._refresh_ui)

    def start(self) -> None:
        """Starts the Tkinter event loop."""
        self._is_running = True
        self._root.after(50, self._refresh_ui)
        self._root.mainloop()

    def stop(self) -> None:
        """Stops the Tkinter event loop and destroys the window."""
        self._is_running = False
        try:
            self._root.destroy()
        except Exception:
            pass

    def _handle_close(self) -> None:
        """Handles manual window closing by user."""
        self.stop()
        if self._on_close:
            self._on_close()
