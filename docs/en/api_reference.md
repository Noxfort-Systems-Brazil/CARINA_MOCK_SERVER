<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# ⚡ Synapse HFT Protocol: gRPC API Reference & Protobuf Specs

This document specifies the gRPC service contracts, RPC methods, and Protocol Buffer definitions for the **Synapse HFT** protocol implemented by the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](../README.md) | 🏛️ [Architecture](architecture.md) | 🖥️ [Tkinter UI](ui_and_dashboard.md) | 🧪 [Testing](testing.md)

---

## 1. Protocol Overview

The **Synapse HFT** protocol is the high-performance telemetry interface connecting CARINA Core AI controllers to external telemetry sinks, validation harnesses, and simulation environments.

- **Transport:** HTTP/2 over gRPC
- **Wire Serialization:** Protocol Buffers v3 (`proto/synapse_hft.proto`)
- **Default Port:** `50051` (Overridable via `MOCK_SERVER_PORT`)
- **Latency Target:** Sub-millisecond ($< 1\text{ ms}$) per frame ingestion.

---

## 2. Service Definition: `HFTLink`

### 2.1 `Ping`
Performs an instantaneous liveness and health verification check.
- **Request:** `Empty`
- **Response:** `SystemState`
  ```protobuf
  message SystemState {
    bool active = 1;        // Readiness indicator
    string state = 2;       // "IDLE", "READY", "RUNNING", "PAUSED"
    uint64 server_time = 3; // Millisecond epoch timestamp
  }
  ```

### 2.2 `LoadScenario`
Transfers road network topology, map geometry, and signal schedules.
- **Request:** `ScenarioDefinition`
  - `map_hash`: SHA-256 identifier of the map.
  - `graph`: Topology nodes and directed road edges.
  - `geometry`: Visual shape polylines.
  - `map_file_content`: Raw binary data of the road network (SUMO `.net.xml` or `.gz`).
  - `map_file_name`: File name (e.g., `londrina.net.xml.gz`).
- **Response:** `ScenarioStatus` (`accepted`: bool, `message`: string).
- **Behavior:** Persists binary payload to disk via `LocalMapStorage`, invokes `SumoNetParser` to extract lanes and traffic lights (`<tlLogic>`), and transitions state to `"READY"`.

### 2.3 `SystemControl`
Commands the test harness state machine.
- **Request:** `ControlCommand` (`START`, `PAUSE`, `STOP`, `RESET`).
- **Response:** `CommandResponse` (`success`: bool, `new_state`: string).

### 2.4 `StreamTraffic`
High-frequency client streaming delivering continuous packets of edge traffic metrics.
- **Request:** Continuous stream of `TrafficFrame`:
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }

  message EdgeState {
    float occupancy = 1;     // Lane occupancy ratio (0.0 to 1.0)
    float mean_speed = 2;    // Vehicle mean speed in m/s
    int32 queue_length = 3;  // Vehicle queue count
    float density = 4;       // Traffic density
  }
  ```
- **Response:** `SystemState` (returned upon graceful stream close).

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Synapse Protocol Technical Reference • CARINA MOCK SERVER</i>
</div>
