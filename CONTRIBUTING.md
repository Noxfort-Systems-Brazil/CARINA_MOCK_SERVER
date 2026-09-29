# Contributing to CARINA MOCK SERVER

Thank you for your interest in contributing to **CARINA MOCK SERVER** — the High-Frequency Telemetry & Synapse Protocol Test Harness for the Noxfort Systems autonomous mobility ecosystem.

---

## 1. Development Setup

1. Fork the repository and clone your fork locally:
   ```bash
   git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
   cd CARINA_MOCK_SERVER
   ```
2. Create and activate a Python 3.12 virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install development and testing dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

---

## 2. Coding & Architecture Standards

All contributions must strictly adhere to the project's engineering principles:
- **Clean Architecture & SOLID:** Never tightly couple domain services to gRPC or UI. Depend on interfaces declared in `src/core/interfaces.py`.
- **Thread Safety:** Ensure any state modified across gRPC handler threads is protected by proper synchronization primitives.
- **Code Formatting & Linting:** Code must adhere to Ruff rules (`pyproject.toml`):
  ```bash
  ruff check .
  ```

---

## 3. Testing & Verification

Before submitting a Pull Request:
1. Ensure all existing tests pass and maintain test coverage above 80% (target: >95%):
   ```bash
   pytest
   ```
2. If adding new protocol RPCs or storage engines, write corresponding unit and integration tests under `tests/`.

---

## 4. Pull Request Workflow

1. Create a descriptive feature branch from `main`:
   ```bash
   git checkout -b feature/synapse-streaming-enhancement
   ```
2. Write clean commits with conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
3. Open a Pull Request on GitHub detailing your changes, architecture impact, and verification steps.
4. Core maintainers will review the PR. Any modifications to `proto/synapse_hft.proto` will require compatibility review with the CARINA Core AI team.
