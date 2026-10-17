<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🚀 Deployment, Docker & Server Operations

This document covers container packaging with Docker, multi-container orchestration with Docker Compose, and headless host execution for the **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [API Reference](api_reference.md) | 🧪 [Testing](testing.md)

---

## 1. Docker Containerization

The server provides a production-ready `Dockerfile` based on `python:3.12-slim`:
- Lightweight image footprint (< 150 MB).
- Runs in headless mode by default (`--no-gui`).
- Built-in socket health check on port `50051`.

### 1.1 Docker Build and Run
```bash
# Build production image
docker build -t carina-mock-server:latest .

# Run container
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  carina-mock-server:latest
```

---

## 2. Docker Compose Orchestration

The repository includes a ready-to-run `docker-compose.yml`:

```bash
# Start container in detached mode
docker compose up -d --build

# View container logs
docker compose logs -f

# Terminate service
docker compose down
```

---

## 3. Environment Variables

| Variable | Default Value | Description |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | Socket binding interface for gRPC. |
| `MOCK_SERVER_PORT` | `50051` | Listening port for incoming Synapse HFT streams. |
| `MOCK_SERVER_NO_GUI` | `1` (in Docker) | Disables Tkinter GUI and activates headless loop. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Deployment & Containerization Guide • CARINA MOCK SERVER</i>
</div>
