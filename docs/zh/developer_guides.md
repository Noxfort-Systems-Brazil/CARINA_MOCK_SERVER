<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🛠️ 开发者指南与代码维护规范

本文档为开发与维护 **CARINA MOCK SERVER** 的工程师提供工作流、编译与代码质量规范指引。

⬅️ [文档中心主页](../README.md) | 🏛️ [系统架构](architecture.md) | ⚡ [API 参考](api_reference.md) | 🧪 [测试验证](testing.md)

---

## 1. 本地研发环境初始化

```bash
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Protobuf 文件编译

当修改 `proto/synapse_hft.proto` 接口定义后，执行以下指令重新生成 Python 代码：
```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

---

## 3. 扩展前端仪表盘卡片

所有展示卡片均需继承自 `BaseCard` 基类 (`ui/components/base.py`)：
1. 在 `ui/components/` 目录下创建新卡片类。
2. 重写 `update_data(self, snapshot: TelemetrySnapshot)` 数据渲染逻辑。
3. 在 `ui/dashboard.py` 的 `_build_ui()` 方法中实例化并放置组件。

---

## 4. 代码静态检查与格式化

提交代码前请运行 Ruff 静态语法检查：
```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>开发者维护指南 • CARINA MOCK SERVER</i>
</div>
