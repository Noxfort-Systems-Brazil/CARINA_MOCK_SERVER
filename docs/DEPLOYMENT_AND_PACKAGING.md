# 🚀 Deployment & Containerization Guide

This document describes the deployment options, containerization workflows, environment configurations, and health-check monitoring for **CARINA MOCK SERVER**.

⬅️ [Documentation Hub](README.md) | 🏛️ [Architecture](../ARCHITECTURE.md) | ⚡ [API Reference](API_REFERENCE.md) | 🧪 [Testing](TESTING.md)

---

## 1. Containerization Overview

CARINA MOCK SERVER is packaged as a lightweight, secure Docker container based on `python:3.12-slim`. It operates natively in headless mode, making it ideal for CI/CD pipelines, cloud test environments, and local multi-container development networks.

- **Base Image:** `python:3.12-slim`
- **Exposed Port:** `50051` (TCP)
- **Container Footprint:** $< 150\text{ MB}$ uncompressed image size, $< 50\text{ MB}$ runtime RAM usage.
- **Rootless Compatibility:** Capable of running under unprivileged user contexts.

---

## 2. Docker & Docker Compose Setup

### 2.1 Building and Running via Docker
```bash
# Build the production image
docker build -t noxfort/carina-mock-server:latest .

# Run the container exposing port 50051
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  noxfort/carina-mock-server:latest
```

### 2.2 Using Docker Compose
The repository includes a ready-to-use `docker-compose.yml`:

```yaml
version: '3.8'

services:
  mock-server:
    build: .
    container_name: carina_mock_server
    ports:
      - "50051:50051"
    environment:
      - MOCK_SERVER_HOST=0.0.0.0
      - MOCK_SERVER_PORT=50051
      - MOCK_SERVER_NO_GUI=1
    volumes:
      - ./data/maps:/app/data/maps
    restart: unless-stopped
```

To start the service:
```bash
docker compose up -d --build
```

To stop the service:
```bash
docker compose down
```

---

## 3. Container Healthcheck

The Dockerfile implements an automated internal health check probing port 50051:
```dockerfile
HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import socket; s = socket.socket(); s.connect(('127.0.0.1', 50051)); s.close()" || exit 1
```

Inspect health status:
```bash
docker inspect --format='{{json .State.Health}}' carina_mock_server
```

---

## 4. Environment Variables Reference

| Variable | Default Value | Description |
|---|---|---|
| `MOCK_SERVER_HOST` | `[::]` / `0.0.0.0` | Network interface address to bind gRPC server. |
| `MOCK_SERVER_PORT` | `50051` | Port number for incoming Synapse HFT connections. |
| `MOCK_SERVER_NO_GUI` | `0` (or `1` in Docker) | When set to `1`, disables Tkinter GUI and runs in pure headless mode. |

---

## 5. Linux Systemd Service Unit

For non-containerized Linux host deployment:

```ini
# /etc/systemd/system/carina-mock.service
[Unit]
Description=CARINA Mock Server - Synapse HFT Protocol Test Harness
After=network.target

[Service]
Type=simple
User=noxfort
WorkingDirectory=/opt/CARINA_MOCK_SERVER
ExecStart=/opt/CARINA_MOCK_SERVER/.venv/bin/python main.py --no-gui
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1
Environment=MOCK_SERVER_PORT=50051

[Install]
WantedBy=multi-user.target
```

Enable and activate:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now carina-mock.service
```

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Deployment & Containerization Guide • CARINA MOCK SERVER</i>
</div>
