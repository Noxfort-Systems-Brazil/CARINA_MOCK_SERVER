<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — Technical Documentation Suite
### High-Frequency Telemetry & Synapse Protocol Test Harness
*Noxfort Systems — A State Of Art Company*

[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Coverage](https://img.shields.io/badge/Coverage-95.7%25-success?style=flat)](../../tests/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat)](../../LICENSE)

---

🌐 **Languages:** **[🇺🇸 English](README.md)** • **[🇧🇷 Português (Brasil)](../pt-br/README.md)** • **[🇪🇸 Español](../es/README.md)** • **[🇫🇷 Français](../fr/README.md)** • **[🇷🇺 Русский](../ru/README.md)** • **[🇨🇳 简体中文](../zh/README.md)** • **[📚 Documentation Hub](../README.md)**

---

</div>

## Welcome to the Official English Documentation Suite

This directory contains the canonical technical documentation suite for the **CARINA MOCK SERVER** — the official High-Frequency Telemetry (HFT) and Synapse wire protocol test harness in the Noxfort Systems autonomous mobility ecosystem.

Built under rigorous **Clean Architecture** and **SOLID** principles, the Mock Server acts as the benchmark sink and validation server for real-time deep reinforcement learning traffic controllers, digital twins, and industrial hardware gateways.

---

## 📚 Specialized Technical Guides

| Document | Topic & Scope | Core Highlights |
|---|---|---|
| 🏛️ **[System Architecture](architecture.md)** | Architecture Blueprint | Clean Architecture, SOLID interfaces, orchestrating facade (`ReceiverFacade`), thread-pool concurrency, and thread-safe telemetry isolation. |
| ⚡ **[Synapse Protocol API](api_reference.md)** | gRPC & Protobuf Specification | `HFTLink` service methods: `Ping`, `LoadScenario`, `SystemControl`, and bidirectional streaming of real-time traffic frames (`StreamTraffic`). |
| 🗺️ **[Map Storage & SUMO Parser](map_and_topology.md)** | Road Network Ingestion | Binary map persistence (`LocalMapStorage`), gzip decompression, shape extraction, and traffic light parsing (`SumoNetParser`). |
| 🖥️ **[Tkinter Dashboard & Diagnostics](ui_and_dashboard.md)** | Desktop UI & Diagnostics | Modular dark theme dashboard (`#1e1e2e`), sliding-window throughput meter (Hz), zero-value data detection engine, and headless fallback. |
| 🧪 **[Testing & Quality Assurance](testing.md)** | Verification & Test Harness | Automated Pytest suite with 39 tests, >95% code coverage, deterministic gRPC context mocks, and concurrency validation. |
| 🚀 **[Deployment & Containerization](deployment.md)** | Docker & Server Operations | Production Python 3.12-slim Dockerfile, `docker-compose.yml`, socket health checks, environment parameters, and Systemd service unit. |
| 🛠️ **[Developer Guides](developer_guides.md)** | Extension & Maintenance | Local setup, protobuf compilation with `protoc`, creating custom UI cards, and structured logging integration. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Intelligent Mobility Engineering • CARINA MOCK SERVER v1.1.0</i>
</div>
