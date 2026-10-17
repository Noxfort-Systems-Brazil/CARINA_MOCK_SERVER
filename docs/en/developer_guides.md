<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🛠️ Developer & Contributor Guide

This document provides developer guidelines for compiling, extending, and maintaining the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [API Reference](api_reference.md) | 🧪 [Testing](testing.md)

---

## 1. Local Environment Setup

```bash
# Clone the repository
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Protobuf Compilation

If you modify `proto/synapse_hft.proto`, recompile the Python gRPC stubs:

```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

This updates `synapse_hft_pb2.py` and `synapse_hft_pb2_grpc.py`.

---

## 3. Creating Custom Dashboard Cards

All dashboard cards inherit from `BaseCard` (`ui/components/base.py`):
1. Create your card in `ui/components/`.
2. Implement the `update_data(self, snapshot: TelemetrySnapshot)` method.
3. Instantiate and pack your card inside `_build_ui()` in `ui/dashboard.py`.

---

## 4. Linting and Formatting

Run Ruff before submitting pull requests:
```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Developer & Contributor Guide • CARINA MOCK SERVER</i>
</div>
