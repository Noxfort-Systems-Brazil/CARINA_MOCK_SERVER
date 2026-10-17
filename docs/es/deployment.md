<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🚀 Despliegue, Contenedores y Operaciones en Servidor

Este documento describe la configuración de Docker, Docker Compose y despliegue headless para **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](../README.md) | 🏛️ [Arquitectura](architecture.md) | ⚡ [Referencia de la API](api_reference.md) | 🧪 [Pruebas](testing.md)

---

## 1. Contenedores Docker

El proyecto incluye un `Dockerfile` optimizado basado en `python:3.12-slim`:
- Imagen compacta (< 150 MB).
- Ejecución predeterminada en modo headless (`--no-gui`).
- Healthcheck integrado de socket en el puerto `50051`.

### 1.1 Comandos de Construcción y Ejecución
```bash
docker build -t carina-mock-server:latest .
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  carina-mock-server:latest
```

---

## 2. Docker Compose

```bash
docker compose up -d --build
docker compose logs -f
docker compose down
```

---

## 3. Variables de Entorno

| Variable | Valor por Defecto | Descripción |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | Dirección de enlace para el socket gRPC. |
| `MOCK_SERVER_PORT` | `50051` | Puerto de escucha para la telemetría Synapse HFT. |
| `MOCK_SERVER_NO_GUI` | `1` (en contenedores) | Desactiva Tkinter y ejecuta el bucle headless. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guía de Despliegue • CARINA MOCK SERVER</i>
</div>
