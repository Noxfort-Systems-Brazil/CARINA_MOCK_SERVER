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
# File: ui/components/events_card.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class EventsCardComponent(IDashboardComponent):
    """Card component to display recent server events in a Listbox."""

    def __init__(self) -> None:
        self._list_events: Optional[tk.Listbox] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        card_events = tk.Frame(parent, bg=Theme.BG_CARD, padx=12, pady=10)

        tk.Label(
            card_events,
            text="EVENTOS RECENTES",
            font=Theme.FONT_SECTION_HEADER,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        ).pack(anchor="w")

        self._list_events = tk.Listbox(
            card_events,
            bg=Theme.BG_SURFACE,
            fg=Theme.TEXT_MAIN,
            font=Theme.FONT_MONO_SM,
            selectbackground=Theme.BG_ACCENT_HOVER,
            selectforeground=Theme.TEXT_MAIN,
            relief=tk.FLAT,
            height=4,
            borderwidth=0
        )
        self._list_events.pack(fill=tk.BOTH, expand=True, pady=(4, 2))

        lbl_footer = tk.Label(
            card_events,
            text="ℹ️ Gravação completa de cada pacote salva em: mock_server.log",
            font=Theme.FONT_MONO_SM,
            fg=Theme.TEXT_DIM,
            bg=Theme.BG_CARD
        )
        lbl_footer.pack(anchor="w")

        return card_events

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if not self._list_events:
            return

        self._list_events.delete(0, tk.END)
        for evt in snapshot.recent_events[-10:]:
            self._list_events.insert(tk.END, evt)
        self._list_events.yview_moveto(1.0)
