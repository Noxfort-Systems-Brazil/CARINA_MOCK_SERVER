# ⚡ Synapse HFT 协议: gRPC 接口规范与 Protobuf 定义

本文档提供 **CARINA MOCK SERVER** 所实现的 **Synapse HFT**（高频遥测）网络接口与 Protocol Buffers 的技术参考规范。

⬅️ [文档中心主页](../README.md) | 🏛️ [系统架构](architecture.md) | 🖥️ [Tkinter 仪表盘](ui_and_dashboard.md) | 🧪 [测试验证](testing.md)

---

## 1. 协议通信概览

**Synapse HFT** 协议是连接 CARINA 核心控制智能体与下层仿真测试平台、硬件网关及数字孪生系统的高性能骨干数据接口。

- **底层通信传输：** 基于 HTTP/2 的 gRPC 框架。
- **消息序列化：** Protocol Buffers v3 (`proto/synapse_hft.proto`)。
- **默认监听端口：** `50051`（支持通过环境变量 `MOCK_SERVER_PORT` 自定义配置）。
- **性能 SLA 指标：** 单帧数据包接收处理延迟低于 1 毫秒。

---

## 2. `HFTLink` 核心服务接口

### 2.1 `Ping`
用于检测测试服务器的网络连通性与运行状态。
- **请求参数：** `Empty`
- **返回响应：** `SystemState` (`active`, `state`, `server_time`)。

### 2.2 `LoadScenario`
传输路网仿真拓扑结构、矢量几何形状与脱机配时方案。
- **请求参数：** `ScenarioDefinition`（地图哈希、拓扑图节点与边、几何多段线坐标、二进制路网数据文件 `.net.xml`/`.gz`）。
- **返回响应：** `ScenarioStatus` (`accepted`, `message`)。
- **内部处理：** 自动将文件落地存储至磁盘，调度 `SumoNetParser` 提取各车道信息与信号机逻辑 (`<tlLogic>`)，并将系统置为 `"READY"` 状态。

### 2.3 `SystemControl`
控制测试环境的有限状态机切换。
- **请求参数：** `ControlCommand`（动作包含：`START`、`PAUSE`、`STOP`、`RESET`）。
- **返回响应：** `CommandResponse` (`success`, `new_state`)。

### 2.4 `StreamTraffic`
高吞吐量的客户端连续流式数据通道，实时推送车道级动态交通流量。
- **请求参数：** 连续 `TrafficFrame` 数据流：
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }
  ```
- **返回响应：** 数据流结束时返回最终 `SystemState`。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Synapse 协议接口规范 • CARINA MOCK SERVER</i>
</div>
