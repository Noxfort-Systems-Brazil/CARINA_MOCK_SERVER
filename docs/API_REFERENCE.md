<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# ⚡ Synapse HFT Protocol: gRPC API Reference & Wire Specification

This document provides the complete API reference for the **Synapse HFT** (High-Frequency Telemetry) communication protocol implemented by the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](README.md) | 🏛️ [Architecture](../ARCHITECTURE.md) | 🖥️ [Tkinter UI](UI_AND_DASHBOARD.md) | 🧪 [Testing](TESTING.md)

---

## 1. Protocol Architecture & Overview

The **Synapse HFT Protocol** defines the high-speed telemetry link between the CARINA Core AI / Traffic Controller and downstream telemetry sinks, digital twin simulators, and validation servers.

- **Transport:** HTTP/2 over gRPC
- **Serialization:** Protocol Buffers v3 (`proto/synapse_hft.proto`)
- **Default Port:** `50051` (Configurable via `MOCK_SERVER_PORT`)
- **Host Binding:** `[::]` / `0.0.0.0` (Configurable via `MOCK_SERVER_HOST`)
- **Target Ingestion Latency:** $< 1.0\text{ ms}$ per telemetry frame.

---

## 2. gRPC Service: `HFTLink`

```protobuf
syntax = "proto3";

package synapse.hft;

service HFTLink {
  rpc Ping (Empty) returns (SystemState);
  rpc LoadScenario (ScenarioDefinition) returns (ScenarioStatus);
  rpc SystemControl (ControlCommand) returns (CommandResponse);
  rpc StreamTraffic (stream TrafficFrame) returns (SystemState);
}
```

---

## 3. RPC Methods Specification

### 3.1 `Ping`
Performs an instantaneous heartbeat check to determine server availability, connection health, and current state.

- **Request:** `Empty`
  ```protobuf
  message Empty {}
  ```
- **Response:** `SystemState`
  ```protobuf
  message SystemState {
    bool active = 1;        // Indicates server readiness
    string state = 2;       // "IDLE", "READY", "RUNNING", "PAUSED"
    uint64 server_time = 3; // Epoch timestamp in milliseconds
  }
  ```
- **Server Behavior:**
  1. Invokes `telemetry.record_ping()`.
  2. Updates `last_ping_time` and connection badge in UI.
  3. Returns within $< 0.5\text{ ms}$.

---

### 3.2 `LoadScenario`
Uploads a simulated road network topology, map file, and offline traffic schedule to configure the mock server for an experimental run.

- **Request:** `ScenarioDefinition`
  ```protobuf
  message ScenarioDefinition {
    string map_hash = 1;
    TopologyGraph graph = 2;
    MapGeometry geometry = 3;
    bytes map_file_content = 4;
    string map_file_name = 5;
    string peak_schedule_json = 6;
  }
  ```
  - **`TopologyGraph`:** Contains collections of `TopologyNode` (coordinates, type, `tl_logic_id`) and `TopologyEdge` (source, target, length, lanes, max speed, signal group).
  - **`MapGeometry`:** List of `MapShape` coordinates for vector rendering.
  - **`map_file_content`:** Raw bytes of the network file (e.g., SUMO `.net.xml` or `.net.xml.gz`).
- **Response:** `ScenarioStatus`
  ```protobuf
  message ScenarioStatus {
    bool accepted = 1;
    string message = 2;
  }
  ```
- **Server Behavior:**
  1. Validates metadata, extracts node and edge counts.
  2. Persists binary content via `LocalMapStorage` to `data/maps/`.
  3. Executes `SumoNetParser` to extract lanes and traffic light controllers (`<tlLogic>`).
  4. Updates `TelemetryState` (`scenario_loaded = True`, `server_state = "READY"`).

---

### 3.3 `SystemControl`
Directs the operational state machine of the simulation server.

- **Request:** `ControlCommand`
  ```protobuf
  message ControlCommand {
    enum Action {
      UNKNOWN = 0;
      START = 1;
      PAUSE = 2;
      STOP = 3;
      RESET = 4;
    }
    Action action = 1;
  }
  ```
- **Response:** `CommandResponse`
  ```protobuf
  message CommandResponse {
    bool success = 1;
    string new_state = 2;
  }
  ```
- **State Machine Transitions:**
  - `START` $\implies$ Transitions state to `"RUNNING"`. Stream ingestion is activated.
  - `STOP` $\implies$ Transitions state to `"IDLE"`.
  - `PAUSE` $\implies$ Transitions state to `"PAUSED"`.
  - `RESET` $\implies$ Resets telemetry counters to initial zero-state.

---

### 3.4 `StreamTraffic`
High-frequency client-streaming RPC delivering continuous traffic frames containing edge-level metrics across the road network.

- **Request:** Stream of `TrafficFrame`
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }

  message EdgeState {
    float occupancy = 1;     // Road occupancy ratio (0.0 to 1.0)
    float mean_speed = 2;    // Mean speed in meters per second (m/s)
    int32 queue_length = 3;  // Number of queuing vehicles
    float density = 4;       // Vehicle density
  }
  ```
- **Response:** `SystemState` (returned upon stream closure)
- **Zero-Value Data Diagnostics:**
  - If a frame has `sequence_id == 0` or empty edges, it is processed as a pure connection heartbeat.
  - For frames with edges, every edge is evaluated:
    $$\text{is\_active} = (\text{occ} > 10^{-4}) \lor (\text{speed} > 10^{-4}) \lor (\text{queue} > 0) \lor (\text{density} > 10^{-4})$$
  - The server records throughput in Hz using a sliding window:
    $$f_{\text{Hz}} = \frac{N - 1}{t_N - t_1}$$

---

## 4. Error Codes & Connection Resilience

| gRPC Status Code | Cause | Client Remediation |
|---|---|---|
| `OK` (0) | Successful operation | Continue regular streaming. |
| `CANCELLED` (1) | Client abruptly closed stream | Handled gracefully by server without crash. |
| `INVALID_ARGUMENT` (3) | Malformed scenario definition | Verify protobuf message serialization. |
| `UNAVAILABLE` (14) | Server offline or network partitioned | Reconnect with exponential backoff. |

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Synapse HFT Protocol Reference • CARINA MOCK SERVER</i>
</div>
