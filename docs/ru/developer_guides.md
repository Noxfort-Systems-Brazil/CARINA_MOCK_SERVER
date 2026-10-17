<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🛠️ Руководство разработчика и сопровождение кода

В данном документе приведены инструкции для разработчиков по сборке, расширению функционала и тестированию **CARINA MOCK SERVER**.

⬅️ [Главный Хаб Документации](../README.md) | 🏛️ [Архитектура](architecture.md) | ⚡ [Спецификация API](api_reference.md) | 🧪 [Тестирование](testing.md)

---

## 1. Развертывание локального окружения

```bash
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Компиляция Protocol Buffers

При внесении изменений в файл `proto/synapse_hft.proto`:
```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

---

## 3. Добавление новых карточек в интерфейс

Все компоненты интерфейса наследуются от `BaseCard` (`ui/components/base.py`):
1. Создайте модуль карточки в `ui/components/`.
2. Реализуйте метод `update_data(self, snapshot: TelemetrySnapshot)`.
3. Добавьте вызов карточки в метод `_build_ui()` в `ui/dashboard.py`.

---

## 4. Проверка качества кода с помощью Ruff

```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Руководство разработчика • CARINA MOCK SERVER</i>
</div>
