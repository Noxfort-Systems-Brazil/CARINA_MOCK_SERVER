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
# File: ui/components/diagnostics_card.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from tkinter import ttk
from typing import Optional
from src.core.interfaces import TelemetrySnapshot, EdgeSample
from ui.theme import Theme
from ui.components.base import IDashboardComponent

class DiagnosticsCardComponent(IDashboardComponent):
    """
    Central diagnostics card component for values and zero-data detection.
    Includes alert banner, 4 KPI indicators, and sample edge table.
    """

    def __init__(self) -> None:
        self._lbl_zero_banner: Optional[tk.Label] = None
        self._lbl_kpi_active_edges: Optional[tk.Label] = None
        self._lbl_kpi_max_occ: Optional[tk.Label] = None
        self._lbl_kpi_avg_speed: Optional[tk.Label] = None
        self._lbl_kpi_max_queue: Optional[tk.Label] = None
        self._tree_samples: Optional[ttk.Treeview] = None

    def build(self, parent: tk.Misc) -> tk.Widget:
        card_diag = tk.Frame(parent, bg=Theme.BG_CARD, padx=14, pady=12)

        # Title & Zero Alert Banner
        diag_header_frame = tk.Frame(card_diag, bg=Theme.BG_CARD)
        diag_header_frame.pack(fill=tk.X, pady=(0, 8))

        tk.Label(
            diag_header_frame,
            text="🔍 DIAGNÓSTICO DE VALORES (DETECÇÃO DE ZEROS)",
            font=Theme.FONT_SECTION_HEADER,
            fg=Theme.YELLOW,
            bg=Theme.BG_CARD
        ).pack(side=tk.LEFT)

        self._lbl_zero_banner = tk.Label(
            diag_header_frame,
            text="⚪ AGUARDANDO DADOS",
            font=Theme.FONT_STATUS_BADGE,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD_ALT,
            padx=12,
            pady=4
        )
        self._lbl_zero_banner.pack(side=tk.RIGHT)

        # KPI Metrics Row (4 Metrics)
        kpi_row = tk.Frame(card_diag, bg=Theme.BG_CARD)
        kpi_row.pack(fill=tk.X, pady=(4, 10))
        for c in range(4):
            kpi_row.columnconfigure(c, weight=1, uniform="kpi")

        # KPI 1: Active Edges
        kpi_1 = tk.Frame(kpi_row, bg=Theme.BG_CARD_ALT, padx=8, pady=6)
        kpi_1.grid(row=0, column=0, sticky="nsew", padx=3)
        tk.Label(
            kpi_1,
            text="ARESTAS COM DADOS (>0)",
            font=Theme.FONT_KPI_LBL,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD_ALT
        ).pack()
        self._lbl_kpi_active_edges = tk.Label(
            kpi_1,
            text="0 / 0 (0%)",
            font=Theme.FONT_KPI_VAL,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD_ALT
        )
        self._lbl_kpi_active_edges.pack()

        # KPI 2: Max Occupancy
        kpi_2 = tk.Frame(kpi_row, bg=Theme.BG_CARD_ALT, padx=8, pady=6)
        kpi_2.grid(row=0, column=1, sticky="nsew", padx=3)
        tk.Label(
            kpi_2,
            text="MAIOR OCUPAÇÃO",
            font=Theme.FONT_KPI_LBL,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD_ALT
        ).pack()
        self._lbl_kpi_max_occ = tk.Label(
            kpi_2,
            text="0.0%",
            font=Theme.FONT_KPI_VAL,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD_ALT
        )
        self._lbl_kpi_max_occ.pack()

        # KPI 3: Avg Speed
        kpi_3 = tk.Frame(kpi_row, bg=Theme.BG_CARD_ALT, padx=8, pady=6)
        kpi_3.grid(row=0, column=2, sticky="nsew", padx=3)
        tk.Label(
            kpi_3,
            text="VELOCIDADE MÉDIA",
            font=Theme.FONT_KPI_LBL,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD_ALT
        ).pack()
        self._lbl_kpi_avg_speed = tk.Label(
            kpi_3,
            text="0.0 m/s",
            font=Theme.FONT_KPI_VAL,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD_ALT
        )
        self._lbl_kpi_avg_speed.pack()

        # KPI 4: Max Queue
        kpi_4 = tk.Frame(kpi_row, bg=Theme.BG_CARD_ALT, padx=8, pady=6)
        kpi_4.grid(row=0, column=3, sticky="nsew", padx=3)
        tk.Label(
            kpi_4,
            text="MAIOR FILA DE VEÍCULOS",
            font=Theme.FONT_KPI_LBL,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD_ALT
        ).pack()
        self._lbl_kpi_max_queue = tk.Label(
            kpi_4,
            text="0 veíc",
            font=Theme.FONT_KPI_VAL,
            fg=Theme.TEXT_MAIN,
            bg=Theme.BG_CARD_ALT
        )
        self._lbl_kpi_max_queue.pack()

        # Sample Edge Table
        tk.Label(
            card_diag,
            text="Amostra de Arestas do Último Pacote:",
            font=Theme.FONT_BODY_BOLD,
            fg=Theme.TEXT_MUTED,
            bg=Theme.BG_CARD
        ).pack(anchor="w", pady=(4, 4))

        columns = ("edge_id", "occupancy", "speed", "queue", "density", "status")
        self._tree_samples = ttk.Treeview(card_diag, columns=columns, show="headings", height=4)
        self._tree_samples.heading("edge_id", text="Aresta ID")
        self._tree_samples.heading("occupancy", text="Ocupação (%)")
        self._tree_samples.heading("speed", text="Velocidade (m/s)")
        self._tree_samples.heading("queue", text="Fila (veíc)")
        self._tree_samples.heading("density", text="Densidade")
        self._tree_samples.heading("status", text="Diagnóstico")

        self._tree_samples.column("edge_id", width=140, anchor="w")
        self._tree_samples.column("occupancy", width=100, anchor="center")
        self._tree_samples.column("speed", width=110, anchor="center")
        self._tree_samples.column("queue", width=90, anchor="center")
        self._tree_samples.column("density", width=90, anchor="center")
        self._tree_samples.column("status", width=110, anchor="center")
        self._tree_samples.pack(fill=tk.X, expand=False)

        return card_diag

    def _is_sample_zero(self, sample: EdgeSample) -> bool:
        """Determine if an edge sample has all zero values."""
        return (sample.occupancy < 0.0001 and sample.mean_speed < 0.0001 and sample.queue_length == 0)

    def update(self, snapshot: TelemetrySnapshot) -> None:
        if (
            not self._lbl_zero_banner
            or not self._lbl_kpi_active_edges
            or not self._lbl_kpi_max_occ
            or not self._lbl_kpi_avg_speed
            or not self._lbl_kpi_max_queue
            or not self._tree_samples
        ):
            return

        # 1. Zero Diagnostic Banner & KPI
        if snapshot.total_frames == 0:
            self._lbl_zero_banner.config(
                text="⚪ AGUARDANDO STREAM DE TRÁFEGO...",
                fg=Theme.TEXT_MUTED,
                bg=Theme.BG_CARD_ALT
            )
            self._lbl_kpi_active_edges.config(text="0 / 0 (0%)", fg=Theme.TEXT_MAIN)
            self._lbl_kpi_max_occ.config(text="0.0%", fg=Theme.TEXT_MAIN)
            self._lbl_kpi_avg_speed.config(text="0.0 m/s", fg=Theme.TEXT_MAIN)
            self._lbl_kpi_max_queue.config(text="0 veíc", fg=Theme.TEXT_MAIN)
        elif snapshot.all_zeros:
            self._lbl_zero_banner.config(
                text="🔴 ALERTA: TODOS OS VALORES DO FRAME ESTÃO ZERADOS!",
                fg=Theme.RED,
                bg=Theme.RED_BG
            )
            self._lbl_kpi_active_edges.config(text=f"0 / {snapshot.total_edges_in_frame} (0.0%)", fg=Theme.RED)
            self._lbl_kpi_max_occ.config(text="0.0%", fg=Theme.RED)
            self._lbl_kpi_avg_speed.config(text="0.0 m/s", fg=Theme.RED)
            self._lbl_kpi_max_queue.config(text="0 veíc", fg=Theme.RED)
        else:
            pct = (
                (snapshot.active_edges_count / snapshot.total_edges_in_frame * 100)
                if snapshot.total_edges_in_frame > 0
                else 0
            )
            self._lbl_zero_banner.config(
                text=f"🟢 DADOS ATIVOS E VÁLIDOS ({pct:.1f}% com dados)",
                fg=Theme.GREEN,
                bg=Theme.GREEN_BG
            )
            self._lbl_kpi_active_edges.config(
                text=f"{snapshot.active_edges_count} / {snapshot.total_edges_in_frame} ({pct:.1f}%)",
                fg=Theme.GREEN
            )
            self._lbl_kpi_max_occ.config(text=f"{snapshot.max_occupancy * 100:.1f}%", fg=Theme.TEXT_MAIN)
            self._lbl_kpi_avg_speed.config(text=f"{snapshot.mean_speed:.2f} m/s", fg=Theme.TEXT_MAIN)
            self._lbl_kpi_max_queue.config(text=f"{snapshot.max_queue} veíc", fg=Theme.TEXT_MAIN)

        # 2. Update sample table
        self._tree_samples.delete(*self._tree_samples.get_children())
        for sample in snapshot.samples:
            is_zero = self._is_sample_zero(sample)
            status_text = "⚪ Zerado" if is_zero else "🟢 Ativo"
            self._tree_samples.insert(
                "",
                tk.END,
                values=(
                    sample.edge_id,
                    f"{sample.occupancy * 100:.1f}%",
                    f"{sample.mean_speed:.2f}",
                    sample.queue_length,
                    f"{sample.density:.2f}",
                    status_text
                )
            )
