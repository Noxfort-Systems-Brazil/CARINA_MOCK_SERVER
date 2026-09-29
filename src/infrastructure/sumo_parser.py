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
# File: src/infrastructure/sumo_parser.py
# Author: Gabriel Moraes
# Date: 2026-09-29

import os
from typing import Any, Dict, List, Optional, Tuple

from src.core.interfaces import IMapParser, ILogger

class SumoNetParser(IMapParser):
    """
    Parser for SUMO network files (.net.xml) using sumolib.
    Extracts lane geometries (lanes/shapes) and nodes controlled by traffic lights (traffic_light).
    """
    def __init__(self, logger: Optional[ILogger] = None):
        self._logger = logger

    def parse_net_xml(self, file_path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        shapes: List[Dict[str, Any]] = []
        traffic_lights: List[Dict[str, Any]] = []

        if not os.path.exists(file_path):
            if self._logger:
                self._logger.error(f"Arquivo de mapa não encontrado para parsing: {file_path}")
            return shapes, traffic_lights

        try:
            import sumolib
            net = sumolib.net.readNet(file_path, withInternal=True)

            # 1. Extraction of edges / lanes
            for edge in net.getEdges():
                edge_id = edge.getID()
                for lane in edge.getLanes():
                    lane_shape = lane.getShape()
                    if lane_shape:
                        shapes.append({
                            'id': f"{edge_id}_{lane.getID()}",
                            'points': lane_shape
                        })

            # 2. Extraction of traffic lights
            for node in net.getNodes():
                if node.getType() == "traffic_light":
                    coord = node.getCoord()
                    traffic_lights.append({
                        'id': node.getID(),
                        'x': coord[0],
                        'y': coord[1]
                    })

            if self._logger:
                self._logger.info(
                    f"SUMO Parsing concluído com sucesso: {len(shapes)} faixas, {len(traffic_lights)} semáforos.",
                    file=file_path,
                    lanes_count=len(shapes),
                    tls_count=len(traffic_lights)
                )

        except ImportError:
            if self._logger:
                self._logger.warning("sumolib não está instalado. Ignorando extração detalhada de geometria SUMO.")
        except Exception as e:
            if self._logger:
                self._logger.error(f"Falha ao realizar parse com sumolib: {e}", file=file_path)
            raise e

        return shapes, traffic_lights
