# 🧪 Testing & Quality Assurance Guide

This document outlines the testing strategy, test harness architecture, coverage metrics, and validation guidelines for the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](README.md) | 🏛️ [Architecture](../ARCHITECTURE.md) | ⚡ [API Reference](API_REFERENCE.md) | 🚀 [Deployment](DEPLOYMENT_AND_PACKAGING.md)

---

## 1. Testing Philosophy & Quality Standards

To serve as a reliable test harness for the mission-critical CARINA intelligent mobility platform, CARINA MOCK SERVER enforces rigorous automated testing:
- **Test Automation:** 100% executable via `pytest`.
- **Minimum Enforced Coverage:** **80%** (configured in `pyproject.toml` via `--cov-fail-under=80`).
- **Current Test Coverage:** **95.7%** across all source modules (`src/`).
- **Total Test Cases:** 39 unit and integration tests executing in $< 1.0\text{ s}$.

---

## 2. Test Suite Structure (`tests/`)

The test suite is organized into modular files targeting individual layers:

| Test Module | Target Class / Subsystem | Test Scope & Verification Focus |
|---|---|---|
| `test_config.py` | `Config` | Default port/host and `MOCK_SERVER_*` environment overrides. |
| `test_grpc_server.py` | `GrpcServer` | gRPC server initialization, socket binding, thread pool lifecycle, and ping integration. |
| `test_hft_service.py` | `HFTService` | `Ping`, `LoadScenario`, `SystemControl` state transitions, `StreamTraffic` streaming, client cancellations, and exceptions. |
| `test_loggers.py` | `CompositeLogger`, `ConsoleLogger`, `FileLogger` | Log level formatting, multi-target output dispatching, and file rotation. |
| `test_map_storage.py` | `LocalMapStorage` | Binary map storage, directory creation, extension normalization (`.net.xml`, `.net.xml.gz`), error handling. |
| `test_receiver_facade.py` | `ReceiverFacade` | Composition root setup, headless lifecycle, idempotent stopping, and display failure fallback to headless. |
| `test_sumo_parser.py` | `SumoNetParser` | Parsing SUMO network XML files, extracting shapes, lane geometries, traffic lights, and malformed XML handling. |
| `test_telemetry_state.py` | `TelemetryState` | Thread-safety, concurrent lock acquisition, zero-value data detection, frame rate Hz, milestone logging, and connection timeout. |

---

## 3. Running the Test Suite

### 3.1 Standard Test Execution
Run the full test suite with verbose output and coverage report:
```bash
pytest
```

### 3.2 Running Specific Test Modules
```bash
# Test only the HFT gRPC service
pytest tests/test_hft_service.py -v

# Test zero-value data detection & telemetry state
pytest tests/test_telemetry_state.py -v
```

### 3.3 Generating HTML Coverage Reports
```bash
pytest --cov=src --cov-report=html
# View report in your browser
xdg-open htmlcov/index.html
```

---

## 4. Coverage Summary Report

```text
Name                                     Stmts   Miss  Cover   Missing
----------------------------------------------------------------------
src/application/hft_service.py              90      3    97%   126, 150, 159
src/core/config.py                           8      0   100%
src/core/interfaces.py                      43      0   100%
src/core/telemetry_state.py                125      1    99%   118
src/infrastructure/composite_logger.py      17      0   100%
src/infrastructure/console_logger.py        21      0   100%
src/infrastructure/file_logger.py           28      1    96%   37
src/infrastructure/grpc_server.py           39      2    95%   86-87
src/infrastructure/map_storage.py           28      0   100%
src/infrastructure/sumo_parser.py           36      0   100%
src/receiver_facade.py                      76     15    80%   96-98, 103-105...
----------------------------------------------------------------------
TOTAL                                      511     22    96%
Required test coverage of 80% reached. Total coverage: 95.69%
```

---

## 5. Mocking Patterns & Fixtures (`tests/conftest.py`)

- **Mock Servicer Context:** Custom `MockContext` simulates `grpc.ServicerContext` to verify RPC error codes and stream termination without needing a live network interface.
- **Temporary Storage Directory:** Pytest fixture providing temporary directories (`tmp_path`) for isolated file write verification.
- **Deterministic Mock Loggers:** In-memory logger mocks enabling assertions on emitted warning and error events.

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Testing & Quality Assurance Guide • CARINA MOCK SERVER</i>
</div>
