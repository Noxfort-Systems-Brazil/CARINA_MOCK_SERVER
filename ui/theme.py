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
# File: ui/theme.py
# Author: Gabriel Moraes
# Date: October 2026

"""
Modern Dark Mode Theme definitions for Tkinter Dashboard (Catppuccin Mocha / VS Code Dark inspired).
"""

class Theme:
    # Backgrounds
    BG_MAIN = "#1e1e2e"         # Base dark background
    BG_SURFACE = "#181825"      # Deep dark base
    BG_CARD = "#24273a"         # Card / container background
    BG_CARD_ALT = "#313244"     # Secondary container / table header
    BG_ACCENT_HOVER = "#363a4f" # Hover color
    
    # Texts
    TEXT_MAIN = "#cdd6f4"       # Primary text (clean off-white)
    TEXT_MUTED = "#a6adc8"      # Subtitles / Secondary labels
    TEXT_DIM = "#6c7086"        # Disabled / Very faint labels
    
    # Accents & Diagnostic Status Colors
    GREEN = "#a6e3a1"           # Success / Active / Valid Data (Neon Green)
    GREEN_BG = "#1e382b"        # Soft green badge background
    
    RED = "#f38ba8"             # Error / All Zero Alert (Soft Red / Coral)
    RED_BG = "#3e1f28"          # Soft red badge background
    
    YELLOW = "#f9e2af"          # Warning / Idle (Warm Yellow)
    YELLOW_BG = "#3e3723"       # Soft yellow badge background
    
    BLUE = "#89b4fa"            # Accent / Links / Frame Counters (Ice Blue)
    MAUVE = "#cba6f7"           # Secondary Accent (Purple/Mauve)
    
    # Fonts
    FONT_FAMILY = "Segoe UI" if "nt" == __import__("os").name else "DejaVu Sans"
    FONT_MONO = "Consolas" if "nt" == __import__("os").name else "Monospace"
    
    FONT_TITLE = (FONT_FAMILY, 15, "bold")
    FONT_SUBTITLE = (FONT_FAMILY, 11, "bold")
    FONT_SECTION_HEADER = (FONT_FAMILY, 10, "bold")
    FONT_BODY = (FONT_FAMILY, 9)
    FONT_BODY_BOLD = (FONT_FAMILY, 9, "bold")
    FONT_KPI_VAL = (FONT_FAMILY, 18, "bold")
    FONT_KPI_LBL = (FONT_FAMILY, 8)
    FONT_STATUS_BADGE = (FONT_FAMILY, 11, "bold")
    FONT_MONO_SM = (FONT_MONO, 8)
    FONT_MONO_MD = (FONT_MONO, 9)
