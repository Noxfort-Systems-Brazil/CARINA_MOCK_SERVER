<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🧪 Testing & Quality Assurance Guidelines

This document specifies the testing strategy, code coverage requirements, and verification procedures for the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [API Reference](api_reference.md) | 🚀 [Deployment](deployment.md)

---

## 1. Quality Standards & Coverage Metrics

CARINA MOCK SERVER enforces strict automated testing standards to ensure reliability as a mission-critical test harness:
- **Test Runner:** `pytest` with `pytest-cov`.
- **Minimum Coverage Threshold:** **80%** (enforced by `--cov-fail-under=80`).
- **Achieved Coverage:** **95.7%** across all source code in `src/`.
- **Total Tests:** 39 unit and integration tests executing in $< 1.0\text{ s}$.

---

## 2. Test Suite Architecture (`tests/`)

- `test_config.py`: Default ports, host bindings, and environment variable overrides.
- `test_grpc_server.py`: Network server lifecycle, socket binding, and ping RPCs.
- `test_hft_service.py`: `Ping`, `LoadScenario` with map storage, state machine transitions, streaming cancellations, and exceptions.
- `test_loggers.py`: Console, file, and composite logger output dispatching.
- `test_map_storage.py`: Binary map saving, auto-extension handling, and write errors.
- `test_receiver_facade.py`: Orchestrator initialization, headless execution, and GUI display fallback.
- `test_sumo_parser.py`: SUMO XML topology parsing, lane extraction, and error handling.
- `test_telemetry_state.py`: Thread-safety with mutex locks, frame rate calculation, zero-value data detection, and timeouts.

---

## 3. Test Commands

```bash
# Run all tests with coverage report
pytest

# Run specific test module
pytest tests/test_hft_service.py -v

# Generate HTML visual coverage report
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Testing & Quality Assurance Guide • CARINA MOCK SERVER</i>
</div>
