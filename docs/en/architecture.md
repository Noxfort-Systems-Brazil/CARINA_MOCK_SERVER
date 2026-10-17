<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🏛️ CARINA MOCK SERVER: Architecture Blueprint & Software Engineering

This document specifies the internal engineering architecture of the **CARINA MOCK SERVER**: its Clean Architecture layers, SOLID principles, subsystem lifecycles, multithreaded concurrency model, and real-time telemetry diagnostics engine.

⬅️ [Documentation Hub](../README.md) | ⚡ [API Reference](api_reference.md) | 🖥️ [Tkinter UI](ui_and_dashboard.md) | 🧪 [Testing](testing.md)

---

## 1. Architectural Foundations & SOLID Design

The CARINA MOCK SERVER adheres strictly to **Clean Architecture** and **SOLID** principles:

1. **Single Responsibility Principle (SRP):** Each module has a single axis of change:
   - `SumoNetParser`: focuses exclusively on extracting road network XML and traffic lights.
   - `LocalMapStorage`: manages disk writes and gzip decompression for binary maps.
   - `TelemetryState`: encapsulates thread-safe telemetry metrics, throughput calculations, and circular event buffers.
2. **Open/Closed Principle (OCP):** New loggers or storage engines can be attached by implementing the contracts in `src/core/interfaces.py` without modifying the core orchestrator.
3. **Liskov Substitution Principle (LSP):** Loggers (`ConsoleLogger`, `FileLogger`, `CompositeLogger`) satisfy `ILogger` without unexpected side effects.
4. **Interface Segregation Principle (ISP):** Telemetry consumers are segregated:
   - `ITelemetryCollector`: write methods utilized by the gRPC handler.
   - `ITelemetryProvider`: read-only snapshot queries consumed by the graphical interface.
5. **Dependency Inversion Principle (DIP):** High-level services (`HFTService`, `ReceiverFacade`) depend entirely on interface abstractions rather than concrete infrastructure classes.

---

## 2. Layered Component Hierarchy

```mermaid
graph TD
    CLI[main.py / Command-Line Interface] -->|Instantiates| Facade[ReceiverFacade]
    
    subgraph Core Layer ["Core Layer (Abstractions & State)"]
        Interfaces[src/core/interfaces.py]
        Config[src/core/config.py]
        State[src/core/telemetry_state.py<br/>ITelemetryCollector & ITelemetryProvider]
    end

    subgraph Application Layer ["Application Layer (Protocols)"]
        HFT[src/application/hft_service.py<br/>HFTLinkServicer]
    end

    subgraph Infrastructure Layer ["Infrastructure Layer (I/O & Networking)"]
        GRPC[src/infrastructure/grpc_server.py]
        Storage[src/infrastructure/map_storage.py]
        Parser[src/infrastructure/sumo_parser.py]
        Loggers[src/infrastructure/composite_logger.py<br/>ConsoleLogger & FileLogger]
    end

    subgraph Presentation Layer ["Presentation Layer (GUI)"]
        UI[ui/dashboard.py<br/>TkinterDashboard]
        Cards[ui/components/*<br/>Modular UI Cards]
    end

    Facade --> Core Layer
    Facade --> Application Layer
    Facade --> Infrastructure Layer
    Facade --> Presentation Layer

    GRPC -->|Dispatches RPCs| HFT
    HFT -->|Records Metrics| State
    HFT -->|Persists Map| Storage
    HFT -->|Extracts Topology| Parser
    UI -->|Reads Immutable Snapshot| State
```

---

## 3. Concurrency & Synchronization Model

- **gRPC Thread Pool:** `GrpcServer` allocates a `ThreadPoolExecutor(max_workers=10)` to asynchronously service incoming client streams without blocking I/O.
- **Critical Section Isolation:** `TelemetryState` guards all mutable state (sliding-window metrics, frame rates, edge lists, event log) behind a single `threading.Lock()`.
- **Immutable UI Snapshots:** The Tkinter UI thread queries `get_snapshot()` every 250ms, receiving an immutable dataclass (`TelemetrySnapshot`) created inside the lock. Rendering occurs with zero contention on background gRPC threads.
- **Graceful Termination:** `ReceiverFacade` hooks OS signals (`SIGINT`, `SIGTERM`), orchestrating orderly server shutdown and resource deallocation.

---

## 4. Zero-Value Data Detection Engine

In distributed reinforcement learning traffic pipelines, silent transmission failures where frames carry all zeros for occupancy, velocity, and queue lengths can destabilize policy networks.

The Mock Server's diagnostic engine checks every incoming frame:
- Each edge metric is evaluated against $\epsilon = 10^{-4}$.
- If no active edges exist, `all_zeros` is flagged as `True`, triggering a visual warning in the UI and a structured log event.
- Up to 5 active and 3 zero-state edge samples are captured for real-time visual inspection in the dashboard.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Architectural Blueprint • CARINA MOCK SERVER</i>
</div>
