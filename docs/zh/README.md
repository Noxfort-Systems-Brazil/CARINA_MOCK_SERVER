<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — 简体中文技术文档套件
### 高频遥测 (HFT) 与 Synapse 协议工业级验证测试平台
*Noxfort Systems — A State Of Art Company*

[![运行状态](https://img.shields.io/badge/状态-运行中-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![测试覆盖率](https://img.shields.io/badge/覆盖率-95.7%25-success?style=flat)](../../tests/)
[![开源许可证](https://img.shields.io/badge/许可证-Apache_2.0-blue?style=flat)](../../LICENSE)

---

🌐 **语言选择:** **[🇺🇸 English](../en/README.md)** • **[🇧🇷 Português (Brasil)](../pt-br/README.md)** • **[🇪🇸 Español](../es/README.md)** • **[🇫🇷 Français](../fr/README.md)** • **[🇷🇺 Русский](../ru/README.md)** • **[🇨🇳 简体中文](README.md)** • **[📚 文档中心主页](../README.md)**

---

</div>

## 欢迎访问官方简体中文技术文档

本目录汇集了 **CARINA MOCK SERVER** 的完整**简体中文**工程与技术架构文档。该服务是 Noxfort Systems 智能交通移动生态系统中负责高频遥测 (HFT) 与 Synapse 通信协议的核心测试基准平台。

系统严格遵循**整洁架构 (Clean Architecture)** 与 **SOLID 原则**构建，为基于深度强化学习的交通信号控制智能体、数字孪生仿真平台及工业级硬件网关提供低延迟数据接收与仿真验证支持。

---

## 📚 专业技术文档导航

| 核心文档 | 技术领域与范畴 | 重点摘要 |
|---|---|---|
| 🏛️ **[系统核心架构](architecture.md)** | 架构设计蓝图 | 整洁架构分层、SOLID 原则落地、外观协调器 (`ReceiverFacade`)、线程池并发模型与线程安全状态隔离。 |
| ⚡ **[Synapse 协议 API](api_reference.md)** | gRPC 与 Protobuf 规范 | `HFTLink` 服务定义、`Ping`、`LoadScenario`、`SystemControl` 以及亚毫秒级高频双向交通流数据推送 (`StreamTraffic`)。 |
| 🖥️ **[Tkinter 界面与诊断引擎](ui_and_dashboard.md)** | 桌面前端与数据诊断 | 现代深色监控主题 (`#1e1e2e`)、滑动窗口吞吐量频率计 (Hz)、全零数据智能预警引擎以及自动化无头 (Headless) 模式。 |
| 🧪 **[测试与质量保证指南](testing.md)** | 自动化测试与覆盖率 | 包含 39 个单元与集成测试的 Pytest 套件，源码覆盖率超过 95.7%，提供确定性 gRPC 上下文模拟与并发测试。 |
| 🚀 **[容器化与系统部署](deployment.md)** | Docker 与生产运维 | 基于 Python 3.12-slim 的轻量级 Docker 镜像、`docker-compose.yml` 快速编排、Socket 级健康检查与 Systemd 服务。 |
| 🛠️ **[开发者维护指南](developer_guides.md)** | 系统扩展与维护 | 本地环境搭建、使用 `protoc` 编译 `.proto` 接口定义、自定义监控卡片扩展与统一日志记录。 |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>智能交通工程 • CARINA MOCK SERVER v1.1.0</i>
</div>
