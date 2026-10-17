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
# File: ui/components/stream_card.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class StreamCardComponent(IDashboardComponent):
    """Card component to display traffic stream (rate Hz, total frames, sequence ID)."""

    def __init__(self) -> None:
        self._lbl_total_frames: Optional[tk.Label] = None
        self._lbl_frame_rate: Optional[tk.Label] = None
        self._lbl_last_seq: Optional[tk.Label] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        card_stream = tk.Frame(parent, bg=Theme.BG_CARD, padx=12, pady=10)

        tk.Label(
            card_stream,
            text="FLUXO DE TRÁFEGO",
            font=Theme.FONT_SECTION_HEADER,
            fg=Theme.BLUE,
            bg=Theme.BG_CARD
        ).pack(anchor="w")

        self._lbl_total_frames = tk.Label(
            card_stream,
            text="Frames Totais: 0 pacotes",
            font=Theme.FONT_BODY_BOLD,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD
        )
        self._lbl_total_frames.pack(anchor="w", pady=(4, 2))

        self._lbl_frame_rate = tk.Label(
            card_stream,
            text="Taxa: 0.0 Hz (frames/s)",
            font=Theme.FONT_BODY,
            fg=Theme.GREEN,
            bg=Theme.BG_CARD
        )
        self._lbl_frame_rate.pack(anchor="w")

        self._lbl_last_seq = tk.Label(
            card_stream,
            text="Seq ID: -  |  Timestamp: -",
            font=Theme.FONT_MONO_SM,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        )
        self._lbl_last_seq.pack(anchor="w", pady=(2, 0))

        return card_stream

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if not self._lbl_total_frames or not self._lbl_frame_rate or not self._lbl_last_seq:
            return

        self._lbl_total_frames.config(text=f"Frames Totais: {snapshot.total_frames} pacotes")
        self._lbl_frame_rate.config(text=f"Taxa: {snapshot.frame_rate_hz:.1f} Hz (frames/s)")
        self._lbl_last_seq.config(
            text=f"Seq ID: #{snapshot.last_sequence_id}  |  Timestamp: {snapshot.last_timestamp:.2f}s"
        )
