# 🗺️ Road Network Storage & SUMO Topology Parser Guide

This document specifies the road network ingestion, disk storage, and SUMO topology parsing subsystem of the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [API Reference](api_reference.md) | 🖥️ [Tkinter UI](ui_and_dashboard.md)

---

## 1. Overview & System Role

In the CARINA ecosystem, urban traffic networks are simulated using Eclipse SUMO (`.net.xml`). When clients initiate a simulation session via the `LoadScenario` gRPC call, full network topologies and raw binary maps are streamed to the Mock Server.

The subsystem consists of two decoupled components:
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`):** Responsible for saving raw map byte arrays to disk and normalizing file extensions (`.net.xml`, `.net.xml.gz`).
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`):** Parses road network XML via `sumolib`, extracting lane shapes and identifying traffic light systems (`<tlLogic>`).

---

## 2. Binary Map Storage (`LocalMapStorage`)

Implements `IMapStorage` from `src/core/interfaces.py`:
- **Default Directory:** `data/maps/` (auto-created on initialization).
- **Extension Normalization:** Appends `.net.xml` if missing; preserves compressed `.gz` archives.
- **Atomic Disk Writes:** Direct file writing using buffered binary I/O.
- **Path Resolution:** `get_map_path(map_name)` enables rapid re-use of previously stored networks.

---

## 3. SUMO Network XML Parser (`SumoNetParser`)

Implements `IMapParser` to extract network topology:
1. **Lane Geometries:** Reads `net.getEdges()` and `edge.getLanes()`, capturing coordinate arrays (`lane.getShape()`) for downstream vector rendering.
2. **Traffic Lights:** Identifies nodes where `node.getType() == "traffic_light"`, extracting coordinates `(x, y)` and node IDs.
3. **Resilience:** Gracefully handles missing `sumolib` dependencies (`ImportError`) by logging a structured warning without interrupting the server.

---

## 4. UI Dashboard Presentation

Parsed metadata is forwarded to `TelemetryState` and rendered in the **`ScenarioCard`**:
- Active road network filename.
- SHA-256 integrity hash.
- Total count of network nodes and edges.
- Payload file size in kilobytes.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Road Network Storage & Parser Guide • CARINA MOCK SERVER</i>
</div>
