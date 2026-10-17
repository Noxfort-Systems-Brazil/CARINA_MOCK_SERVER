<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🛠️ Guía del Desarrollador y Contribuciones

Este documento proporciona directrices de desarrollo, compilación y extensión para **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](../README.md) | 🏛️ [Arquitectura](architecture.md) | ⚡ [Referencia de la API](api_reference.md) | 🧪 [Pruebas](testing.md)

---

## 1. Configuración del Entorno Local

```bash
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Compilación de Protobuf

Para compilar cambios en `proto/synapse_hft.proto`:
```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

---

## 3. Creación de Nuevas Tarjetas para el Panel

Todas las tarjetas heredan de `BaseCard` (`ui/components/base.py`):
1. Cree la clase en `ui/components/`.
2. Implemente el método `update_data(self, snapshot: TelemetrySnapshot)`.
3. Regístrela en `_build_ui()` dentro de `ui/dashboard.py`.

---

## 4. Calidad de Código con Ruff

```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guía del Desarrollador • CARINA MOCK SERVER</i>
</div>
