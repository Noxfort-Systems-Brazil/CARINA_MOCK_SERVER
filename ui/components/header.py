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
# File: ui/components/header.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class HeaderComponent(IDashboardComponent):
    """Header component with application title and connection status badge."""

    def __init__(self) -> None:
        self._lbl_header_status: Optional[tk.Label] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        header_frame = tk.Frame(parent, bg=Theme.BG_SURFACE, padx=14, pady=10, relief=tk.FLAT)

        title_label = tk.Label(
            header_frame,
            text="📡 CARINA MOCK SERVER  |  TELEMETRIA SYNAPSE",
            font=Theme.FONT_TITLE,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_SURFACE
        )
        title_label.pack(side=tk.LEFT)

        self._lbl_header_status = tk.Label(
            header_frame,
            text="● AGUARDANDO CONEXÃO",
            font=Theme.FONT_STATUS_BADGE,
            fg=Theme.YELLOW,
            bg=Theme.YELLOW_BG,
            padx=10,
            pady=4
        )
        self._lbl_header_status.pack(side=tk.RIGHT)

        return header_frame

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if not self._lbl_header_status:
            return

        if snapshot.connected:
            if snapshot.total_frames > 0:
                self._lbl_header_status.config(
                    text="● CONECTADO & RECEBENDO",
                    fg=Theme.GREEN,
                    bg=Theme.GREEN_BG
                )
            else:
                self._lbl_header_status.config(
                    text="● CONECTADO",
                    fg=Theme.GREEN,
                    bg=Theme.GREEN_BG
                )
        else:
            self._lbl_header_status.config(
                text="● AGUARDANDO SYNAPSE",
                fg=Theme.YELLOW,
                bg=Theme.YELLOW_BG
            )
