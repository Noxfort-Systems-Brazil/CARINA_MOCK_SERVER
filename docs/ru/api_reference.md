<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# ⚡ Протокол Synapse HFT: Спецификация API gRPC и Protobuf

В данном документе приведено детальное описание сетевого контракта gRPC и структур Protocol Buffers протокола **Synapse HFT** для **CARINA MOCK SERVER**.

⬅️ [Главный Хаб Документации](../README.md) | 🏛️ [Архитектура](architecture.md) | 🖥️ [Панель управления Tkinter](ui_and_dashboard.md) | 🧪 [Тестирование](testing.md)

---

## 1. Обзор протокола

Протокол **Synapse HFT** предназначен для передачи потоковой телеметрии с ультранизкими задержками между интеллектуальным ядром CARINA и внешними стендами валидации или симуляторами.

- **Транспорт:** HTTP/2 поверх gRPC.
- **Формат данных:** Protocol Buffers v3 (`proto/synapse_hft.proto`).
- **Сетевой порт:** `50051` (настраивается переменной `MOCK_SERVER_PORT`).
- **Целевая задержка:** менее 1 миллисекунды на кадр.

---

## 2. Методы сервиса `HFTLink`

### 2.1 `Ping`
Быстрая проверка доступности и рабочего состояния сервера.
- **Входные данные:** `Empty`
- **Ответ:** `SystemState` (`active`, `state`, `server_time`).

### 2.2 `LoadScenario`
Загрузка графа дорожной сети, геометрии и расписаний светофоров.
- **Входные данные:** `ScenarioDefinition` (хеш карты, узлы и ребра, геометрия, бинарное содержимое карты SUMO `.net.xml`/`.gz`).
- **Ответ:** `ScenarioStatus` (`accepted`, `message`).
- **Логика:** Сохранение карты на диск, вызов `SumoNetParser` для извлечения полос и светофоров (`<tlLogic>`), перевод в состояние `"READY"`.

### 2.3 `SystemControl`
Управление конечным автоматом симуляции.
- **Входные данные:** `ControlCommand` (`START`, `PAUSE`, `STOP`, `RESET`).
- **Ответ:** `CommandResponse` (`success`, `new_state`).

### 2.4 `StreamTraffic`
Непрерывная передача потока телеметрии дорожного движения.
- **Входные данные:** Поток `TrafficFrame`:
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }
  ```
- **Ответ:** `SystemState` при штатном закрытии потока.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Спецификация протокола Synapse • CARINA MOCK SERVER</i>
</div>
