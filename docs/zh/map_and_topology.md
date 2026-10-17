<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🗺️ 路网地图持久化与 SUMO 拓扑解析引擎指南

本文档阐述 **CARINA MOCK SERVER** 的路网文件接收持久化及 SUMO 交通仿真拓扑解析子系统。

⬅️ [文档中心主页](README.md) | 🏛️ [系统架构](architecture.md) | ⚡ [API 参考](api_reference.md) | 🖥️ [Tkinter 仪表盘](ui_and_dashboard.md)

---

## 1. 子系统概述与业务角色

在 CARINA 智能交通生态中，仿真路网统一采用 Eclipse SUMO (`.net.xml`) 格式。当测试端发起 `LoadScenario` gRPC 请求时，完整的二进制文件及拓扑结构将实时传输至测试服务器。

系统通过两层基础设施解耦处理：
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`)：** 负责二进制数据流的磁盘持久化与扩展名标准化 (`.net.xml`, `.net.xml.gz`)。
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`)：** 调用 `sumolib` 提取车道矢量折线几何与受控信号机节点 (`<tlLogic>`)。

---

## 2. 二进制存储管理 (`LocalMapStorage`)

实现 `IMapStorage` 接口 (`src/core/interfaces.py`)：
- **存储目录：** 默认为 `data/maps/`（如不存在将自动建立）。
- **扩展名补全：** 若传入文件名缺少扩展名则自动补齐 `.net.xml`，原生支持 `.gz` 压缩格式。
- **存储操作：** 直接基于系统底层进行原子二进制文件写入。

---

## 3. SUMO 拓扑解析器 (`SumoNetParser`)

实现 `IMapParser` 接口：
1. **车道几何形状：** 遍历路网中的边与车道，提取坐标折线点集 (`lane.getShape()`) 供矢量渲染。
2. **交通信号灯：** 过滤识别类型为 `"traffic_light"` 的节点，提取物理坐标与控制器编号。
3. **环境兼容与容错：** 当运行环境中缺少 `sumolib` 依赖时自动捕获异常并记录日志，确保 gRPC 服务不中断。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>路网存储与拓扑解析指南 • CARINA MOCK SERVER</i>
</div>
