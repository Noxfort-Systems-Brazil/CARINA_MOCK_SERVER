# 🖥️ Tkinter Desktop Dashboard & Telemetry Diagnostics

This document details the user interface architecture, dark visual theme, and real-time telemetry diagnostics engine of the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [API Reference](api_reference.md) | 🧪 [Testing](testing.md)

---

## 1. User Interface Architecture

The CARINA MOCK SERVER provides a desktop dashboard implemented in native **Python Tkinter**, structured into decoupled, modular cards styled with the Noxfort dark theme (`ui/theme.py`).

### 1.1 Non-Blocking Polling Loop
The root window schedules periodic updates every **250 milliseconds** via `self.root.after(250, self._update_loop)`:
- Queries an immutable `TelemetrySnapshot` from `TelemetryState`.
- Zero lock contention on the gRPC streaming threads.

---

## 2. Dashboard Components

1. **Header (`ui/components/header.py`):** Displays ecosystem branding and an active/idle connection status badge.
2. **Connection Card (`ui/components/connection_card.py`):** Displays gRPC host/port, current server state (`IDLE`, `RUNNING`), and time elapsed since last heartbeat.
3. **Scenario Card (`ui/components/scenario_card.py`):** Shows loaded map filename, integrity hash, node/edge counts, and file size.
4. **Stream Card (`ui/components/stream_card.py`):** Shows total frames ingested, last sequence ID, and packet rate (Hz) computed over a 20-sample rolling window.
5. **Diagnostics Card (`ui/components/diagnostics_card.py`):** Real-time zero-value data detection banner (🟢 ACTIVE DATA vs ⚠️ ALL ZERO DATA), active edge count, max occupancy %, mean speed (m/s), and edge sample inspection table.
6. **Events Card (`ui/components/events_card.py`):** Circular feed displaying the 15 most recent server events.

---

## 3. Headless Mode Operation

For containerized environments, cloud VMs, and CI/CD pipelines lacking an X11/Wayland display server:
```bash
# Via CLI flag
python main.py --no-gui

# Via environment variable
MOCK_SERVER_NO_GUI=1 python main.py
```
If Tkinter fails to initialize due to a missing display, the server automatically catches the exception and falls back to headless mode.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>UI & Diagnostics Guide • CARINA MOCK SERVER</i>
</div>
