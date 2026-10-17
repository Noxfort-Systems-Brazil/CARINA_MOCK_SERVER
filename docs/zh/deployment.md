<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🚀 容器化构建、Docker 编排与系统运维

本文档提供 **CARINA MOCK SERVER** 的 Docker 镜像构建、Docker Compose 编排与服务运维指引。

⬅️ [文档中心主页](../README.md) | 🏛️ [系统架构](architecture.md) | ⚡ [API 参考](api_reference.md) | 🧪 [测试验证](testing.md)

---

## 1. Docker 容器化

服务采用基于官方 `python:3.12-slim` 定制的轻量镜像：
- 镜像压缩体积小于 150 MB。
- 容器内默认以无头模式运行 (`--no-gui`)。
- 内置针对 `50051` 端口的 Socket 健康检查机制。

### 1.1 镜像构建与启动
```bash
docker build -t carina-mock-server:latest .
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  carina-mock-server:latest
```

---

## 2. Docker Compose 编排

```bash
docker compose up -d --build
docker compose logs -f
docker compose down
```

---

## 3. 系统环境变量一览

| 变量名称 | 默认值 | 作用说明 |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | gRPC 服务绑定的主机网络接口。 |
| `MOCK_SERVER_PORT` | `50051` | 接收 Synapse HFT 遥测数据的监听端口。 |
| `MOCK_SERVER_NO_GUI` | `1` (容器环境) | 强制关闭图形化组件并启用命令行循环。 |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>部署与运维指南 • CARINA MOCK SERVER</i>
</div>
