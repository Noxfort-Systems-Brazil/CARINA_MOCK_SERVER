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
