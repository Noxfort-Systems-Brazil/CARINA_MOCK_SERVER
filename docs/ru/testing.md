<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🧪 Тестирование и обеспечение качества

В данном документе изложены стратегия тестирования, требования к покрытию кода и методы валидации компонентов **CARINA MOCK SERVER**.

⬅️ [Главный Хаб Документации](../README.md) | 🏛️ [Архитектура](architecture.md) | ⚡ [Спецификация API](api_reference.md) | 🚀 [Развертывание](deployment.md)

---

## 1. Стандарты качества и покрытие кода

- **Среда тестирования:** `pytest` с модулем `pytest-cov`.
- **Минимальный порог покрытия:** **80%** (параметр `--cov-fail-under=80`).
- **Фактическое покрытие:** **95.7%** по всей кодовой базе в `src/`.
- **Общее число тестов:** 39 модульных и интеграционных тестов с временем выполнения до 1 секунды.

---

## 2. Структура тестовых модулей (`tests/`)

- `test_config.py`: Значения по умолчанию и переопределение переменных окружения.
- `test_grpc_server.py`: Запуск, остановка сетевого сервера и вызовы ping.
- `test_hft_service.py`: Проверка RPC-методов, сохранение карт, обработка прерываний и ошибок потока.
- `test_loggers.py`: Логирование в консоль, ротируемый файл и композитный вывод.
- `test_map_storage.py`: Запись бинарных карт, проверка расширений и защита от ошибок записи.
- `test_receiver_facade.py`: Инициализация фасада и штатный переход в headless-режим.
- `test_sumo_parser.py`: Парсинг топологии SUMO XML и устойчивость к поврежденным файлам.
- `test_telemetry_state.py`: Многопоточный доступ с блокировками, расчет Гц, детектор нулей и тайм-ауты.

---

## 3. Команды запуска тестов

```bash
# Полный запуск с отчетом о покрытии
pytest

# Запуск одного модуля
pytest tests/test_hft_service.py -v

# Создание подробного HTML-отчета
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Обеспечение качества и тестирование • CARINA MOCK SERVER</i>
</div>
