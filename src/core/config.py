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
# File: src/core/config.py
# Author: Gabriel Moraes
# Date: October 2026

import os

class Config:
    def __init__(self):
        # Allow override via environment variables
        self.port = int(os.getenv("MOCK_SERVER_PORT", "50051"))
        self.host = os.getenv("MOCK_SERVER_HOST", "[::]")

    @property
    def server_address(self) -> str:
        return f"{self.host}:{self.port}"
