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
# File: ui/components/scenario_card.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class ScenarioCardComponent(IDashboardComponent):
    """Card component to display scenario data and loaded map."""

    def __init__(self) -> None:
        self._lbl_scenario_name: Optional[tk.Label] = None
        self._lbl_scenario_details: Optional[tk.Label] = None
        self._lbl_scenario_hash: Optional[tk.Label] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        card_scenario = tk.Frame(parent, bg=Theme.BG_CARD, padx=12, pady=10)

        tk.Label(
            card_scenario,
            text="CENÁRIO / MAPA RECEBIDO",
            font=Theme.FONT_SECTION_HEADER,
            fg=Theme.MAUVE,
            bg=Theme.BG_CARD
        ).pack(anchor="w")

        self._lbl_scenario_name = tk.Label(
            card_scenario,
            text="Arquivo: Nenhum cenário carregado",
            font=Theme.FONT_BODY_BOLD,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD
        )
        self._lbl_scenario_name.pack(anchor="w", pady=(4, 2))

        self._lbl_scenario_details = tk.Label(
            card_scenario,
            text="Nós: 0  |  Arestas: 0  |  Tamanho: 0 KB",
            font=Theme.FONT_BODY,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        )
        self._lbl_scenario_details.pack(anchor="w")

        self._lbl_scenario_hash = tk.Label(
            card_scenario,
            text="Hash: -",
            font=Theme.FONT_MONO_SM,
            fg=Theme.TEXT_DIM,
            bg=Theme.BG_CARD
        )
        self._lbl_scenario_hash.pack(anchor="w")

        return card_scenario

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if not self._lbl_scenario_name or not self._lbl_scenario_details or not self._lbl_scenario_hash:
            return

        if snapshot.scenario_loaded:
            size_kb = snapshot.file_size_bytes / 1024
            self._lbl_scenario_name.config(text=f"Arquivo: {snapshot.map_name}")
            self._lbl_scenario_details.config(
                text=f"Nós: {snapshot.nodes_count}  |  Arestas: {snapshot.edges_count}  |  Tamanho: {size_kb:.1f} KB"
            )
            self._lbl_scenario_hash.config(
                text=f"Hash: {snapshot.map_hash[:20]}..." if snapshot.map_hash else "Hash: -"
            )
        else:
            self._lbl_scenario_name.config(text="Arquivo: Nenhum cenário carregado")
            self._lbl_scenario_details.config(text="Nós: 0  |  Arestas: 0  |  Tamanho: 0 KB")
            self._lbl_scenario_hash.config(text="Hash: -")
