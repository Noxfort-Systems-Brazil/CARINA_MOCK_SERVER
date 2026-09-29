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
# File: src/infrastructure/map_storage.py
# Author: Gabriel Moraes
# Date: 2026-09-29

import os
from typing import Optional

from src.core.interfaces import IMapStorage, ILogger

class LocalMapStorage(IMapStorage):
    """
    Manages local storage of map files received via gRPC.
    Ensures files are saved in the appropriate directory (e.g. data/maps/).
    """
    def __init__(self, storage_dir: str = "data/maps", logger: Optional[ILogger] = None):
        self._storage_dir = os.path.abspath(storage_dir)
        self._logger = logger
        self._ensure_storage_dir()

    def _ensure_storage_dir(self) -> None:
        os.makedirs(self._storage_dir, exist_ok=True)

    def save_map(self, map_name: str, content: bytes) -> str:
        safe_name = os.path.basename(map_name) if map_name else "received_map.net.xml"
        if not safe_name.endswith(".xml") and not safe_name.endswith(".xml.gz"):
            safe_name = f"{safe_name}.net.xml"

        file_path = os.path.join(self._storage_dir, safe_name)
        try:
            with open(file_path, "wb") as f:
                f.write(content)
            if self._logger:
                self._logger.info(
                    f"Arquivo de mapa salvo com sucesso ({len(content)} bytes)",
                    file_path=file_path,
                    size_bytes=len(content)
                )
        except Exception as e:
            if self._logger:
                self._logger.error(f"Erro ao salvar arquivo de mapa: {e}", file_path=file_path)
            raise e

        return file_path

    def get_map_path(self, map_name: str) -> Optional[str]:
        file_path = os.path.join(self._storage_dir, os.path.basename(map_name))
        return file_path if os.path.exists(file_path) else None
