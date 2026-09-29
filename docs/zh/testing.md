# 🧪 自动化测试与质量保证指南

本文档规定 **CARINA MOCK SERVER** 的自动化测试规范、测试用例结构及覆盖率衡量标准。

⬅️ [文档中心主页](../README.md) | 🏛️ [系统架构](architecture.md) | ⚡ [API 参考](api_reference.md) | 🚀 [部署运维](deployment.md)

---

## 1. 质量基准与代码覆盖率

- **测试框架：** `pytest` 配合 `pytest-cov`。
- **强制覆盖率门槛：** 最低 **80%**（在 `pyproject.toml` 中配置 `--cov-fail-under=80`）。
- **当前实际覆盖率：** `src/` 核心代码达 **95.7%**。
- **测试规模：** 39 个单元及集成测试用例，总耗时低于 1 秒。

---

## 2. 测试模块结构 (`tests/`)

- `test_config.py`：默认配置解析与环境变量覆盖测试。
- `test_grpc_server.py`：网络服务生命周期启停与 Ping 连通测试。
- `test_hft_service.py`：RPC 接口响应、场景文件保存、流量数据流与异常处理测试。
- `test_loggers.py`：控制台、文件日志及复合日志记录行为验证。
- `test_map_storage.py`：二进制地图写入、文件扩展名容错与异常拦截。
- `test_receiver_facade.py`：顶层协调器初始化与无头降级逻辑测试。
- `test_sumo_parser.py`：SUMO XML 拓扑结构解析与破损文件鲁棒性测试。
- `test_telemetry_state.py`：多线程并发锁竞争、吞吐量计算与全零数据诊断。

---

## 3. 测试运行指令

```bash
# 运行完整测试套件并输出覆盖率报告
pytest

# 执行特定测试文件
pytest tests/test_hft_service.py -v

# 导出详细的 HTML 可视化覆盖率报告
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>测试规范与质量保证 • CARINA MOCK SERVER</i>
</div>
