<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🛠️ Developer & Contributor Guides

This document provides developer guidelines for maintaining, extending, and testing the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](README.md) | 🏛️ [Architecture](../ARCHITECTURE.md) | ⚡ [API Reference](API_REFERENCE.md) | 🧪 [Testing](TESTING.md)

---

## 1. Local Development Environment

```bash
# Clone and enter directory
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER

# Initialize virtual environment with Python 3.12
python3 -m venv .venv
source .venv/bin/activate

# Install runtime and dev dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Compiling Protocol Buffers

If you modify `proto/synapse_hft.proto`, recompile the Python protobuf and gRPC stubs:

```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

Verify that `proto/synapse_hft_pb2.py` and `proto/synapse_hft_pb2_grpc.py` update cleanly.

---

## 3. Extending the gRPC Interface

To add a new RPC method (e.g., `GetDiagnostics`):

1. **Update `proto/synapse_hft.proto`:**
   ```protobuf
   service HFTLink {
     // ... existing RPCs
     rpc GetDiagnostics (Empty) returns (DiagnosticsReport);
   }
   ```
2. **Recompile Protobuf:** Run the command in Section 2.
3. **Update Interface (`src/core/interfaces.py`):** Add any necessary state queries to `ITelemetryProvider`.
4. **Implement Method in `HFTService` (`src/application/hft_service.py`):**
   ```python
   def GetDiagnostics(self, request, context):
       snapshot = self._telemetry.get_snapshot()
       return pb2.DiagnosticsReport(...)
   ```
5. **Add Automated Unit Tests:** Add a test case to `tests/test_hft_service.py`.

---

## 4. Creating a New UI Card Component

All visual dashboard cards inherit from `BaseCard` (`ui/components/base.py`):

```python
# ui/components/custom_metric_card.py
import tkinter as tk
from ui.components.base import BaseCard
from src.core.interfaces import TelemetrySnapshot

class CustomMetricCard(BaseCard):
    def __init__(self, parent):
        super().__init__(parent, title="CUSTOM METRICS")
        self.label = tk.Label(self.body, text="Waiting...", bg="#181825", fg="#cdd6f4")
        self.label.pack(anchor="w", padx=10, pady=5)

    def update_data(self, snapshot: TelemetrySnapshot) -> None:
        self.label.config(text=f"Total Packets: {snapshot.total_frames}")
```

Register your card inside `TkinterDashboard._build_ui()` in `ui/dashboard.py`.

---

## 5. Linting and Code Quality

Run Ruff before submitting any pull request:
```bash
ruff check .
ruff format --check .
```

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Developer & Contributor Guide • CARINA MOCK SERVER</i>
</div>
