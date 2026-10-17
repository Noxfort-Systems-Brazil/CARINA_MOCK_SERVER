<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# Changelog — CARINA MOCK SERVER

All notable changes to the CARINA MOCK SERVER project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-09-29

### Added
- **Zero-Value Data Diagnostic Engine:** Real-time anomaly detection checking if incoming `TrafficFrame` packages contain real traffic flow or empty zeros.
- **Sliding-Window Throughput Meter (Hz):** Real-time measurement of ingestion frequency across a 20-frame rolling window.
- **Modern Tkinter Dark GUI:** Modular card-based dashboard (`#1e1e2e`) with live connection status, scenario metrics, stream telemetry, live edge inspection table, and rolling event logs.
- **Transparent Headless Fallback:** Automatic headless execution when running in Docker, CI/CD, or systems without X11 displays.
- **SUMO Topology & Map Parser:** Binary storage engine (`LocalMapStorage`) and XML parser (`SumoNetParser`) extracting shapes and traffic lights (`<tlLogic>`).
- **Comprehensive Documentation Suite:** Multi-language documentation covering English, Portuguese (BR), Spanish, French, Russian, and Mandarin Chinese.

### Changed
- Refactored server core to Clean Architecture and strict SOLID interfaces in `src/core/interfaces.py`.
- Refactored `ReceiverFacade` to serve as a pure composition root and lifecycle orchestrator.

### Fixed
- Idempotent server shutdown and graceful signal handling (`SIGINT`, `SIGTERM`).
- Thread-safe telemetry snapshot isolation avoiding GUI race conditions.

---

## [1.0.0] - 2026-05-02

### Added
- Initial release of CARINA Synapse HFT Mock Server.
- Basic implementation of `synapse_hft.proto` with `Ping`, `LoadScenario`, `SystemControl`, and `StreamTraffic` RPCs.
- Standalone gRPC service on port 50051.
