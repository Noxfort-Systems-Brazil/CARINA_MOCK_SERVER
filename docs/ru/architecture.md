<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🏛️ CARINA MOCK SERVER: Архитектура системы и принципы проектирования

Данный документ описывает внутреннюю архитектуру **CARINA MOCK SERVER**: распределение по слоям Чистой Архитектуры, применение принципов SOLID, модель многопоточности и систему диагностики телеметрии в реальном времени.

⬅️ [Главный Хаб Документации](../README.md) | ⚡ [Спецификация API](api_reference.md) | 🖥️ [Интерфейс Tkinter](ui_and_dashboard.md) | 🧪 [Тестирование](testing.md)

---

## 1. Архитектурные принципы и структура SOLID

CARINA MOCK SERVER строго следует принципам **Чистой Архитектуры** и **SOLID**:

1. **Единственная ответственность (SRP):** Каждый модуль решает строго изолированную задачу:
   - `SumoNetParser`: парсинг графа дорожной сети SUMO и светофорных объектов.
   - `LocalMapStorage`: запись файлов карт на диск и распаковка gzip.
   - `TelemetryState`: потокобезопасное хранение метрик и скользящих окон частоты.
2. **Открытость/Закрытость (OCP):** Новые типы логгеров или хранилищ подключаются через интерфейсы `src/core/interfaces.py` без изменения ядра.
3. **Подстановка Барбары Лисков (LSP):** Все реализации логгеров (`ConsoleLogger`, `FileLogger`, `CompositeLogger`) полностью взаимозаменяемы.
4. **Разделение интерфейсов (ISP):**
   - `ITelemetryCollector`: методы записи для gRPC-обработчика.
   - `ITelemetryProvider`: методы чтения снимков состояния для графического интерфейса.
5. **Инверсия зависимостей (DIP):** Высокоуровневые сервисы (`HFTService`, `ReceiverFacade`) зависят исключительно от интерфейсных контрактов.

---

## 2. Схема компонентов и потоков данных

```mermaid
graph TD
    CLI[main.py / CLI] -->|Инициализирует| Facade[ReceiverFacade]
    
    subgraph Слой Core ["Слой Core (Абстракции и состояние)"]
        Interfaces[src/core/interfaces.py]
        Config[src/core/config.py]
        State[src/core/telemetry_state.py]
    end

    subgraph Слой Приложения ["Слой Приложения (Протоколы)"]
        HFT[src/application/hft_service.py]
    end

    subgraph Слой Инфраструктуры ["Слой Инфраструктуры (Ввод/Вывод и сеть)"]
        GRPC[src/infrastructure/grpc_server.py]
        Storage[src/infrastructure/map_storage.py]
        Parser[src/infrastructure/sumo_parser.py]
        Loggers[src/infrastructure/composite_logger.py]
    end

    subgraph Слой Отображения ["Слой Отображения (GUI)"]
        UI[ui/dashboard.py]
        Cards[ui/components/*]
    end

    Facade --> Слой Core
    Facade --> Слой Приложения
    Facade --> Слой Инфраструктуры
    Facade --> Слой Отображения

    GRPC -->|Маршрутизирует RPC| HFT
    HFT -->|Записывает телеметрию| State
    HFT -->|Сохраняет карту| Storage
    HFT -->|Парсит топологию| Parser
    UI -->|Читает неизменяемый снимок| State
```

---

## 3. Модель параллелизма и синхронизации

- **Пул потоков gRPC:** Сервер обрабатывает входящие потоки в `ThreadPoolExecutor(max_workers=10)` без блокировки ввода-вывода.
- **Изоляция с мьютексом:** Все разделяемые переменные в `TelemetryState` защищены блокировкой `threading.Lock()`.
- **Неизменяемые снимки (Snapshots):** Поток интерфейса Tkinter с интервалом 250 мс запрашивает метод `get_snapshot()`, получающий неизменяемый dataclass без задержек сетевых потоков.
- **Корректное завершение:** `ReceiverFacade` перехватывает сигналы ОС (`SIGINT`, `SIGTERM`), гарантируя безопасное закрытие сокетов и файлов.

---

## 4. Движок обнаружения нулевых данных

При отладке нейросетевых моделей управления движением опасной аномалией являются пустые пакеты телеметрии (где занятость, скорость и очереди равны 0 во всей сети).

Диагностический движок проверяет каждый кадр:
- Каждое ребро дорожной сети сверяется с порогом $\epsilon = 10^{-4}$.
- При отсутствии активных данных флаг `all_zeros` переводится в `True`, что сразу отображается предупреждением в интерфейсе и записывается в журнал.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Спецификация архитектуры • CARINA MOCK SERVER</i>
</div>
