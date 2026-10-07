# 🗺️ Хранилище карт и парсер топологии SUMO

В данном документе описана подсистема сохранения бинарных карт и синтаксического анализа графа дорожной сети SUMO в **CARINA MOCK SERVER**.

⬅️ [Главный Хаб Документации](README.md) | 🏛️ [Архитектура](architecture.md) | ⚡ [Спецификация API](api_reference.md) | 🖥️ [Интерфейс Tkinter](ui_and_dashboard.md)

---

## 1. Роль подсистемы в экосистеме

В проекте CARINA дорожные сети моделируются в формате Eclipse SUMO (`.net.xml`). При запуске испытаний клиент передает топологию через gRPC-метод `LoadScenario`.

Обработка выполняется двумя компонентами:
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`):** Запись бинарного содержимого на диск и нормализация расширений (`.net.xml`, `.net.xml.gz`).
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`):** Извлечение полос движения и светофоров (`<tlLogic>`) с помощью библиотеки `sumolib`.

---

## 2. Дисковое хранилище (`LocalMapStorage`)

Реализует интерфейс `IMapStorage` (`src/core/interfaces.py`):
- **Каталог по умолчанию:** `data/maps/` (создается автоматически).
- **Расширения:** Автоматическое добавление `.net.xml` и поддержка gzip-архивов `.gz`.
- **Запись на диск:** Прямой бинарный ввод-вывод потоков байтов.

---

## 3. Парсер сети SUMO (`SumoNetParser`)

Реализует интерфейс `IMapParser`:
1. **Геометрия полос:** Чтение ребер и координат полос (`lane.getShape()`) для последующей векторной отрисовки.
2. **Светофорные объекты:** Поиск узлов типа `"traffic_light"` с сохранением координат `(x, y)` и ID.
3. **Отказоустойчивость:** Безопасный перехват `ImportError` при отсутствии `sumolib` без остановки сервера.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Руководство по топологии и картам • CARINA MOCK SERVER</i>
</div>
