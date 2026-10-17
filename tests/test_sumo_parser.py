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
# File: tests/test_sumo_parser.py
# Author: Gabriel Moraes
# Date: October 2026

import os
import pytest
from src.infrastructure.sumo_parser import SumoNetParser
from tests.conftest import InMemoryLogger

def test_sumo_parser_file_not_found():
    logger = InMemoryLogger()
    parser = SumoNetParser(logger=logger)
    shapes, tls = parser.parse_net_xml("non_existent_file.net.xml")

    assert shapes == []
    assert tls == []
    assert any(log[0] == "ERROR" and "não encontrado" in log[1] for log in logger.logs)

def test_sumo_parser_with_sample_osm_map():
    sample_map = os.path.abspath("data/maps/osm.net.xml.gz")
    if not os.path.exists(sample_map):
        pytest.skip("data/maps/osm.net.xml.gz não encontrado")

    logger = InMemoryLogger()
    parser = SumoNetParser(logger=logger)
    shapes, tls = parser.parse_net_xml(sample_map)

    # Verify that sumolib successfully loaded sample map geometries
    assert len(shapes) > 0
    assert "id" in shapes[0]
    assert "points" in shapes[0]
    assert any(log[0] == "INFO" and "SUMO Parsing concluído" in log[1] for log in logger.logs)

def test_sumo_parser_invalid_file(tmp_path):
    invalid_file = tmp_path / "corrupted.net.xml"
    invalid_file.write_text("Not valid XML at all")

    logger = InMemoryLogger()
    parser = SumoNetParser(logger=logger)

    with pytest.raises(Exception):
        parser.parse_net_xml(str(invalid_file))

    assert any(log[0] == "ERROR" and "Falha ao realizar parse" in log[1] for log in logger.logs)

def test_sumo_parser_import_error(monkeypatch, tmp_path):
    valid_file = tmp_path / "empty.net.xml"
    valid_file.write_text("<net></net>")

    import builtins
    real_import = builtins.__import__

    def mock_import(name, *args, **kwargs):
        if name == "sumolib":
            raise ImportError("No module named 'sumolib'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", mock_import)

    logger = InMemoryLogger()
    parser = SumoNetParser(logger=logger)
    shapes, tls = parser.parse_net_xml(str(valid_file))

    assert shapes == []
    assert tls == []
    assert any(log[0] == "WARNING" and "sumolib não está instalado" in log[1] for log in logger.logs)
