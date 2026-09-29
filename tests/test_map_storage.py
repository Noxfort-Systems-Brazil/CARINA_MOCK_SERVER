import os
import pytest
from src.infrastructure.map_storage import LocalMapStorage
from tests.conftest import InMemoryLogger

def test_map_storage_save_and_retrieve(tmp_path):
    logger = InMemoryLogger()
    storage = LocalMapStorage(storage_dir=str(tmp_path), logger=logger)

    content = b"<net>Test Map XML Content</net>"
    saved_path = storage.save_map("custom_map.xml", content)

    assert os.path.exists(saved_path)
    assert saved_path == str(tmp_path / "custom_map.xml")
    assert storage.get_map_path("custom_map.xml") == saved_path

    with open(saved_path, "rb") as f:
        assert f.read() == content

    assert any("Arquivo de mapa salvo com sucesso" in log[1] for log in logger.logs)

def test_map_storage_auto_extension(tmp_path):
    storage = LocalMapStorage(storage_dir=str(tmp_path))
    saved_path = storage.save_map("no_extension_name", b"binary")

    assert saved_path.endswith("no_extension_name.net.xml")
    assert os.path.exists(saved_path)

def test_map_storage_gz_extension(tmp_path):
    storage = LocalMapStorage(storage_dir=str(tmp_path))
    saved_path = storage.save_map("city.xml.gz", b"binary_gz")

    assert saved_path.endswith("city.xml.gz")
    assert os.path.exists(saved_path)

def test_map_storage_non_existent(tmp_path):
    storage = LocalMapStorage(storage_dir=str(tmp_path))
    assert storage.get_map_path("non_existent_map.xml") is None

def test_map_storage_write_error(tmp_path, monkeypatch):
    logger = InMemoryLogger()
    storage = LocalMapStorage(storage_dir=str(tmp_path), logger=logger)

    def mock_open(*args, **kwargs):
        raise PermissionError("Disk is write protected")

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(PermissionError):
        storage.save_map("test.xml", b"content")

    assert any(log[0] == "ERROR" and "Erro ao salvar" in log[1] for log in logger.logs)
