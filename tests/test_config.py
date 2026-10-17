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
# File: tests/test_config.py
# Author: Gabriel Moraes
# Date: October 2026

from src.core.config import Config

def test_config_defaults(monkeypatch):
    monkeypatch.delenv("MOCK_SERVER_PORT", raising=False)
    monkeypatch.delenv("MOCK_SERVER_HOST", raising=False)
    cfg = Config()
    assert cfg.port == 50051
    assert cfg.host == "[::]"
    assert cfg.server_address == "[::]:50051"

def test_config_custom_env(monkeypatch):
    monkeypatch.setenv("MOCK_SERVER_PORT", "9999")
    monkeypatch.setenv("MOCK_SERVER_HOST", "127.0.0.1")
    cfg = Config()
    assert cfg.port == 9999
    assert cfg.host == "127.0.0.1"
    assert cfg.server_address == "127.0.0.1:9999"
