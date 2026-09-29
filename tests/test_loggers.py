import os
from src.infrastructure.console_logger import ConsoleLogger
from src.infrastructure.file_logger import FileLogger
from src.infrastructure.composite_logger import CompositeLogger
from tests.conftest import InMemoryLogger

def test_console_logger(caplog):
    logger = ConsoleLogger()
    with caplog.at_level("DEBUG"):
        logger.info("Test info message", detail="val1")
        logger.warning("Test warn message")
        logger.error("Test error message", code=500)
        logger.debug("Test debug message")

    assert "Test info message | detail=val1" in caplog.text
    assert "Test warn message" in caplog.text
    assert "Test error message | code=500" in caplog.text

def test_file_logger(tmp_path):
    log_file = tmp_path / "test.log"
    logger = FileLogger(filepath=str(log_file))

    logger.info("File info test", metric=100)
    logger.warning("File warn test")
    logger.error("File error test")
    logger.debug("File debug test")

    assert os.path.exists(log_file)
    content = log_file.read_text(encoding="utf-8")
    assert "File info test | metric=100" in content
    assert "File warn test" in content
    assert "File error test" in content

def test_composite_logger():
    log1 = InMemoryLogger()
    log2 = InMemoryLogger()
    composite = CompositeLogger([log1, log2])

    composite.info("Broadcast info", key="a")
    composite.warning("Broadcast warning")
    composite.error("Broadcast error", code=404)
    composite.debug("Broadcast debug")

    for logger in [log1, log2]:
        assert len(logger.logs) == 4
        levels = [entry[0] for entry in logger.logs]
        assert levels == ["INFO", "WARNING", "ERROR", "DEBUG"]
        assert logger.logs[0][1] == "Broadcast info"
        assert logger.logs[0][2] == {"key": "a"}
