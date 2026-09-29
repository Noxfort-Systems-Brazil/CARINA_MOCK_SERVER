---
tags: [home, index, carina, mock_server, hub]
aliases: [Documentation Index, Overview, Portal]
---

# 🚗 CARINA MOCK SERVER Documentation Hub

Welcome to the technical documentation library for **CARINA MOCK SERVER** (High-Frequency Telemetry & Synapse Protocol Test Harness) — part of the **CARINA** intelligent transportation ecosystem developed by **Noxfort Systems**.

Designed to operate seamlessly on **GitHub** and as an **[Obsidian](https://obsidian.md/) Knowledge Vault**, this documentation suite covers Clean Architecture patterns, the sub-millisecond Synapse HFT gRPC wire protocol, SUMO network topology ingestion, real-time zero-value diagnostics, and multi-platform containerized deployments.

---

## 🗺️ Master Navigation & Modules

| Subsystem / Dimension | Focus Area | Direct Link |
| :--- | :--- | :---: |
| 📚 **Master Map of Content** | Primary Obsidian Hub & Codebase Directory Map | [Explore Hub](CARINA_MOCK_MOC.md) |
| 🏛️ **System Architecture** | Clean Architecture, SOLID Principles, Facade & Concurrency | [View Blueprint](../ARCHITECTURE.md) |
| ⚡ **Synapse HFT API** | Sub-millisecond gRPC Telemetry & Protobuf Specifications | [View API Reference](API_REFERENCE.md) |
| 🖥️ **Desktop UI & Diagnostics** | Modern Dark Tkinter Dashboard, Card Components & Zero-Data Alert | [View UI Guide](UI_AND_DASHBOARD.md) |
| 🧪 **Testing & Validation** | Pytest Test Suite, Harness Mocks & Coverage Reporting | [View Testing](TESTING.md) |
| 🚀 **Deployment & Packaging** | Docker Containerization, Compose & Headless Operation | [View Deployment](DEPLOYMENT_AND_PACKAGING.md) |
| 🛠️ **Developer Guides** | Protobuf Compilation, Extending RPCs & Custom Modules | [View Guides](DEVELOPER_GUIDES.md) |

---

## ⚡ Quick Architecture Summary

```text
       ┌────────────────────────────────────────────────────────┐
       │               CARINA MOCK SERVER ENGINE                │
       │     (gRPC HFT Ingestion & Telemetry Verification)      │
       └──────────────────────────┬─────────────────────────────┘
                                  │
      ┌───────────────────────────┼───────────────────────────┐
      ▼                           ▼                           ▼
┌──────────────┐          ┌──────────────┐          ┌──────────────────┐
│  gRPC Server │          │TelemetryState│          │  LocalMapStorage │
│(Port 50051)  │ ◄──────► │ (Zero-Diag)  │ ◄──────► │ (SUMO .net.xml)  │
└──────┬───────┘          └──────┬───────┘          └──────────────────┘
       │                         │
       ▼                         ▼
┌──────────────┐          ┌──────────────┐
│  HFTService  │          │   Tkinter    │
│(Protobuf IPC)│          │  Dashboard   │
└──────────────┘          └──────────────┘
```

---

## 🌐 Multi-Language Documentation

Select your preferred language for localized technical guides:
- [🇺🇸 English (Canonical)](en/README.md)
- [🇧🇷 Português do Brasil](pt-br/README.md)
- [🇪🇸 Español](es/README.md)
- [🇫🇷 Français](fr/README.md)
- [🇷🇺 Русский](ru/README.md)
- [🇨🇳 简体中文](zh/README.md)
