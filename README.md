---
tags: [readme, home, carina, mock_server]
aliases: [CARINA Mock Server, Root]
---

<div align="center">

<img src="docs/assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="130" />

# CARINA MOCK SERVER
### High-Frequency Telemetry & Synapse Protocol Test Harness
*Noxfort Systems — A State Of Art Company*

[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Protocol Buffers](https://img.shields.io/badge/Protobuf-v4.25%2B-blue?style=flat)](https://protobuf.dev/)
[![Coverage](https://img.shields.io/badge/Coverage-95.7%25-success?style=flat)](tests/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat)](LICENSE)

---

🌐 **Translations / Idiomas:** **[🇺🇸 English](docs/en/README.md)** • **[🇧🇷 Português do Brasil](docs/pt-br/README.md)** • **[🇪🇸 Español](docs/es/README.md)** • **[🇫🇷 Français](docs/fr/README.md)** • **[🇷🇺 Русский](docs/ru/README.md)** • **[🇨🇳 简体中文](docs/zh/README.md)** • **[📚 Documentation Hub](docs/README.md)**

---

</div>

**CARINA MOCK SERVER** is the industrial-grade High-Frequency Telemetry (HFT) and Synapse Protocol Test Harness for the CARINA intelligent transportation ecosystem. Built in Python 3.12 under strict **Clean Architecture** and **SOLID** principles, it serves as the official telemetry sink, topology validator, and stress-testing server for real-time traffic control agents, digital twins, and hardware gateways.

---

## 📚 Documentation Hub & Knowledge Vault

Explore the full architecture, internal mechanics, protocol specifications, and developer guides:

| Card / Subsystem | Focus Area | Direct Link |
| :--- | :--- | :---: |
| 📚 **Documentation Hub** | Central Multi-Language Index & Direct Topic Matrix | [Explore Hub](docs/README.md) |
| 🗺️ **Master MOC** | Master Map of Content & Obsidian Knowledge Vault index | [View MOC](docs/CARINA_MOCK_MOC.md) |
| 🏛️ **Core Architecture** | Clean Architecture, SOLID interfaces, Facade & Concurrency | [View Blueprint](ARCHITECTURE.md) |
| ⚡ **Synapse HFT API** | gRPC `HFTLink` interface (`Ping`, `LoadScenario`, `Control`, `Stream`) | [View API Reference](docs/API_REFERENCE.md) |
| 🗺️ **Map Storage & SUMO Parser** | Binary Road Map Ingestion & Traffic Light Topology Parsing | [View Map Guide](docs/MAP_AND_TOPOLOGY.md) |
| 🖥️ **Tkinter Dashboard & UI** | Desktop dark GUI, telemetry sliding window & zero-value diagnostics | [View UI Guide](docs/UI_AND_DASHBOARD.md) |
| 🧪 **Testing & Quality Assurance** | Pytest harness, 39 tests, coverage (>95%), and mocks | [View Guidelines](docs/TESTING.md) |
| 🚀 **Deployment & Containerization** | Docker multi-stage build, Docker Compose, headless operation | [View Deployment](docs/DEPLOYMENT_AND_PACKAGING.md) |
| 🛠️ **Developer Guides** | Protobuf compilation, extending RPCs, custom UI widgets | [View Guides](docs/DEVELOPER_GUIDES.md) |

---

## ⚡ Key Architectural Capabilities

- **Synapse HFT Link (Sub-Millisecond gRPC):** High-throughput, low-latency implementation of `synapse_hft.proto` supporting concurrent RPC pings, scenario uploads, system commands (`START`, `PAUSE`, `STOP`, `RESET`), and bidirectional frame streaming (`StreamTraffic`).
- **Real-Time Zero-Value Data Diagnostics:** Automatically analyzes incoming frames across hundreds of urban lanes to distinguish healthy real-time traffic from empty or unpopulated zero-state telemetry.
- **Sliding-Window Throughput Meter (Hz):** Real-time packet frequency monitor measuring network streaming throughput over a 20-sample sliding window.
- **SUMO Network Topology Ingestion:** Binary payload extraction and parsing of SUMO road networks (`.net.xml`, `.net.xml.gz`), extracting lanes, shapes, and traffic light systems (`<tlLogic>`).
- **Pure Architectural Facade (`ReceiverFacade`):** Single, decoupled orchestrator coordinating gRPC lifecycle, composite logging (`ConsoleLogger`, `FileLogger`), thread-safe telemetry state, and user interface.
- **Dual Presentation Engine:** Rich desktop dark-themed Tkinter dashboard (`#1e1e2e`) with live visual metric cards, with transparent fallback to headless mode (`--no-gui` / `MOCK_SERVER_NO_GUI=1`) for headless servers, Docker containers, and CI/CD pipelines.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.12+
- `pip` or virtual environment manager
- Tkinter (standard on Windows/macOS; on Debian/Ubuntu: `sudo apt-get install python3-tk`)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install runtime dependencies
pip install -r requirements.txt

# Install development & test dependencies (optional)
pip install -r requirements-dev.txt
```

### 3. Running with Desktop GUI
```bash
python main.py
```

### 4. Running in Headless Mode (CLI / Servers)
```bash
python main.py --no-gui
# Alternatively via environment variable:
MOCK_SERVER_NO_GUI=1 python main.py
```

### 5. Running with Docker & Docker Compose
```bash
# Build and run containerized server on port 50051
docker compose up --build -d

# Check server logs
docker compose logs -f
```

---

## 🧪 Running Automated Tests

```bash
# Run pytest with code coverage validation (strict minimum 80%)
pytest
```

---

<div align="center">
  <img src="docs/assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="48" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>High-Frequency Telemetry & Synapse Protocol Test Harness • CARINA MOCK SERVER v1.1.0</i><br/>
  <small>Licensed under the <a href="LICENSE">Apache License 2.0</a>. © 2026 Noxfort Systems.</small>
</div>
