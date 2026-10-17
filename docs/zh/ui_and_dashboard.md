<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🖥️ Tkinter 桌面监控面板与实时遥测诊断

本文档详细介绍 **CARINA MOCK SERVER** 的桌面前端交互架构、深色视觉主题以及实时数据异常诊断引擎。

⬅️ [文档中心主页](../README.md) | 🏛️ [系统架构](architecture.md) | ⚡ [API 参考](api_reference.md) | 🧪 [测试验证](testing.md)

---

## 1. 前端设计与刷新机制

监控面板基于 Python 原生 **Tkinter** 框架构建，采用卡片化布局结构并搭配 Noxfort 经典工控深色调 (`ui/theme.py`)。

### 1.1 非阻塞周期性轮询
主窗口通过 `self.root.after(250, self._update_loop)` 每隔 **250 毫秒** 触发一次 UI 刷新：
- 从 `TelemetryState` 读取只读不可变的 `TelemetrySnapshot`。
- 渲染过程不占用网络传输通道，确保前端不卡顿、后台高吞吐。

---

## 2. 界面卡片组件

1. **顶部状态栏 (`ui/components/header.py`)：** 展示生态系统徽标与连接状态指示灯。
2. **连接卡片 (`ui/components/connection_card.py`)：** 实时呈现 gRPC 监听网络地址、当前系统运行模式以及心跳延迟。
3. **路网场景卡片 (`ui/components/scenario_card.py`)：** 显示加载的仿真地图名称、完整性哈希校验值、节点及路段总数和文件体积。
4. **数据流卡片 (`ui/components/stream_card.py`)：** 统计接收帧总数、序列号以及基于滑动窗口计算的瞬时频率 (Hz)。
5. **诊断卡片 (`ui/components/diagnostics_card.py`)：** 全零数据预警横幅（🟢 正常活跃数据 vs ⚠️ 全零异常数据）、活跃路段统计与实时采样明细表格。
6. **事件日志卡片 (`ui/components/events_card.py`)：** 滚动记录最近 15 条系统关键运行事件。

---

## 3. 无头模式 (Headless 命令行运行)

在云服务器、Docker 容器以及无 X11 图形环境的 CI/CD 流程中：
```bash
python main.py --no-gui
# 或配置环境变量：
MOCK_SERVER_NO_GUI=1 python main.py
```
当检测到无法打开图形窗口时，系统会自动平滑降级至无头模式继续稳定提供 gRPC 服务。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>界面设计与诊断指南 • CARINA MOCK SERVER</i>
</div>
