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
# File: ui/components/connection_card.py
# Author: Gabriel Moraes
# Date: 2026-09-29

import tkinter as tk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class ConnectionCardComponent(IDashboardComponent):
    """Card component to display server state and ping/frame timing."""

    def __init__(self) -> None:
        self._lbl_conn_state: Optional[tk.Label] = None
        self._lbl_last_ping: Optional[tk.Label] = None
        self._lbl_last_frame_time: Optional[tk.Label] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        card_conn = tk.Frame(parent, bg=Theme.BG_CARD, padx=12, pady=10)

        tk.Label(
            card_conn,
            text="ESTADO & CONEXÃO",
            font=Theme.FONT_SECTION_HEADER,
            fg=Theme.BLUE,
            bg=Theme.BG_CARD
        ).pack(anchor="w")

        self._lbl_conn_state = tk.Label(
            card_conn,
            text="Estado: IDLE",
            font=Theme.FONT_BODY_BOLD,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD
        )
        self._lbl_conn_state.pack(anchor="w", pady=(4, 2))

        self._lbl_last_ping = tk.Label(
            card_conn,
            text="Último Ping: Nenhum",
            font=Theme.FONT_BODY,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        )
        self._lbl_last_ping.pack(anchor="w")

        self._lbl_last_frame_time = tk.Label(
            card_conn,
            text="Último Frame: Aguardando...",
            font=Theme.FONT_BODY,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        )
        self._lbl_last_frame_time.pack(anchor="w")

        return card_conn

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if not self._lbl_conn_state or not self._lbl_last_ping or not self._lbl_last_frame_time:
            return

        self._lbl_conn_state.config(text=f"Estado: {snapshot.server_state}")

        if snapshot.time_since_last_ping is not None:
            self._lbl_last_ping.config(text=f"Último Ping: há {snapshot.time_since_last_ping:.1f}s")
        else:
            self._lbl_last_ping.config(text="Último Ping: Nenhum recebido")

        if snapshot.time_since_last_frame is not None:
            self._lbl_last_frame_time.config(text=f"Último Frame: há {snapshot.time_since_last_frame:.1f}s")
        else:
            self._lbl_last_frame_time.config(text="Último Frame: Nenhum recebido")
