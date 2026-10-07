---
tags: [moc, hub, docs, obsidian, carina, mock_server, index]
aliases: [CARINA Mock MOC, Master Documentation Hub, Documentation Index, Knowledge Vault]
---

# 📚 CARINA MOCK SERVER Technical Master Documentation Hub

Welcome to the **CARINA MOCK SERVER** technical documentation library. Designed as an industrial test harness for High-Frequency Telemetry (HFT) and the Synapse wire protocol, this server validates high-throughput traffic control agents, digital twin simulations, and hardware gateway integrity.

This master documentation index provides deep technical coverage for core developers, traffic systems engineers, and QA automation teams. It is fully compatible with both **GitHub** and **[Obsidian](https://obsidian.md/)**.

---

## 🗺️ Codebase Map & Directory Hierarchy

```text
CARINA_MOCK_SERVER/
├── main.py                     # Application Entrypoint & CLI Parser (--no-gui flag)
├── ARCHITECTURE.md             # Clean Architecture Blueprint, Layers & Sequence Flow
├── pyproject.toml              # Pytest configuration, coverage thresholds (min 80%), Ruff
├── requirements.txt            # Python production dependencies (grpcio, protobuf)
├── requirements-dev.txt        # Development dependencies (pytest, pytest-cov, ruff)
├── Dockerfile                  # Containerized deployment image (Python 3.12-slim)
├── docker-compose.yml          # Container orchestration service mapping port 50051
├── LICENSE                     # Apache License 2.0
├── mock_server.log             # Rotating log file output
│
├── proto/                      # gRPC Protocol Specifications
│   ├── synapse_hft.proto       # Protocol buffer definitions (HFTLink, Messages)
│   ├── synapse_hft_pb2.py      # Compiled Protobuf message classes
│   └── synapse_hft_pb2_grpc.py # Compiled gRPC client & servicer stubs
│
├── src/                        # Core Application Source Code
│   ├── receiver_facade.py      # Master Orchestrator Facade (Composition Root)
│   ├── core/                   # Domain Core & Interfaces
│   │   ├── interfaces.py       # Abstract Base Classes (ILogger, ITelemetry, IMap, etc.)
│   │   ├── config.py           # Environment-aware configuration (Host, Port)
│   │   └── telemetry_state.py  # Thread-safe telemetry store & zero-value diagnostics
│   ├── application/            # Protocol & Service Implementations
│   │   └── hft_service.py      # HFTLinkServicer gRPC implementation
│   └── infrastructure/         # External Systems, I/O & Parsers
│       ├── grpc_server.py      # ThreadPool gRPC server lifecycle management
│       ├── map_storage.py      # Binary map persistence engine (SUMO .net.xml.gz)
│       ├── sumo_parser.py      # XML topology parser & traffic light extractor
│       ├── composite_logger.py # Multi-destination logger (Console + File)
│       ├── console_logger.py   # Colored terminal output logger
│       └── file_logger.py      # Timestamped persistent file logger
│
├── ui/                         # Presentation Layer (Tkinter Desktop Dashboard)
│   ├── dashboard.py            # Tkinter root window, periodic refresh loop (250ms)
│   ├── theme.py                # Noxfort dark palette (#1e1e2e, #11111b, #a6e3a1)
│   └── components/             # Reusable modular UI card components
│       ├── base.py             # BaseCard abstract widget
│       ├── header.py           # Top status bar with live connection badge
│       ├── connection_card.py  # gRPC address, status & server uptime
│       ├── scenario_card.py    # Map name, hash, node/edge counts & file size
│       ├── stream_card.py      # Total frames, sequence ID & throughput (Hz)
│       ├── diagnostics_card.py # Zero-value data alert & edge sample table
│       └── events_card.py      # Rolling event log feed
│
├── tests/                      # Automated Testing Suite (Pytest)
│   ├── conftest.py             # Shared fixtures and mock objects
│   ├── test_config.py          # Config environment variable overrides
│   ├── test_grpc_server.py     # gRPC server lifecycle & ping tests
│   ├── test_hft_service.py     # HFTService RPC methods & stream scenarios
│   ├── test_loggers.py         # Console, File & Composite logger tests
│   ├── test_map_storage.py     # Binary map saving & retrieval tests
│   ├── test_receiver_facade.py # Facade orchestrator & headless fallback tests
│   ├── test_sumo_parser.py     # XML network parser & error resilience tests
│   └── test_telemetry_state.py # Thread-safety, sliding window & zero-data tests
│
└── docs/                       # Knowledge Vault & Multi-Language Suite
    ├── README.md               # Central Documentation Hub
    ├── index.md                # MkDocs Portal
    ├── CARINA_MOCK_MOC.md      # Master Map of Content (This Document)
    ├── API_REFERENCE.md        # Synapse HFT Protocol & RPC Specification
    ├── MAP_AND_TOPOLOGY.md     # SUMO Map Storage & Topology Parser Guide
    ├── UI_AND_DASHBOARD.md     # Tkinter Dashboard, Dark Theme & Diagnostics
    ├── TESTING.md              # Pytest Suite, Coverage & Mocks Guide
    ├── DEPLOYMENT_AND_PACKAGING.md # Docker, Compose & Headless Setup
    ├── DEVELOPER_GUIDES.md     # Developer Setup, Protoc & Card Expansion
    ├── stylesheets/            # Custom Material for MkDocs CSS
    ├── assets/                 # Brand logos (CARINA, Noxfort)
    ├── pt-br/                  # Portuguese (Brazil) documentation
    ├── en/                     # English canonical documentation
    ├── es/                     # Spanish documentation
    ├── fr/                     # French documentation
    ├── ru/                     # Russian documentation
    └── zh/                     # Simplified Chinese documentation
```

---

## 🎯 Master Topic Navigation

- **Core Architecture & Clean Layers:** [`ARCHITECTURE.md`](ARCHITECTURE.md)
- **gRPC API Reference:** [`API_REFERENCE.md`](API_REFERENCE.md)
- **Map Storage & Topology Parser:** [`MAP_AND_TOPOLOGY.md`](MAP_AND_TOPOLOGY.md)
- **Dashboard & Diagnostics:** [`UI_AND_DASHBOARD.md`](UI_AND_DASHBOARD.md)
- **Testing & Coverage:** [`TESTING.md`](TESTING.md)
- **Deployment & Containers:** [`DEPLOYMENT_AND_PACKAGING.md`](DEPLOYMENT_AND_PACKAGING.md)
- **Developer Guides:** [`DEVELOPER_GUIDES.md`](DEVELOPER_GUIDES.md)

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Master Map of Content • CARINA MOCK SERVER v1.1.0</i>
</div>
