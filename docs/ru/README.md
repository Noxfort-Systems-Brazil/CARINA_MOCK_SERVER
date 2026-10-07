<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — Комплект технической документации
### Тестовый стенд высокочастотной телеметрии (HFT) и валидации протокола Synapse
*Noxfort Systems — A State Of Art Company*

[![Статус](https://img.shields.io/badge/Статус-Активен-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Покрытие](https://img.shields.io/badge/Покрытие-95.7%25-success?style=flat)](../../tests/)
[![Лицензия](https://img.shields.io/badge/Лицензия-Apache_2.0-blue?style=flat)](../../LICENSE)

---

🌐 **Языки:** **[🇺🇸 English](../en/README.md)** • **[🇧🇷 Português (Brasil)](../pt-br/README.md)** • **[🇪🇸 Español](../es/README.md)** • **[🇫🇷 Français](../fr/README.md)** • **[🇷🇺 Русский](README.md)** • **[🇨🇳 简体中文](../zh/README.md)** • **[📚 Главный Хаб Документации](../README.md)**

---

</div>

## Добро пожаловать в официальную документацию на русском языке

В данном каталоге собрана полная техническая документация на **русском языке** для **CARINA MOCK SERVER** — официального испытательного стенда высокочастотной телеметрии (HFT) и протокола Synapse в экосистеме умного управления дорожным движением Noxfort Systems.

Сервер построен в строгом соответствии с принципами **Чистой Архитектуры** и **SOLID**. Он выполняет роль валидатора и тестового приемника телеметрии для нейросетевых агентов глубокого обучения с подкреплением, цифровых двойников и физических дорожных контроллеров.

---

## 📚 Каталог технических руководств

| Документ | Тематика и охват | Ключевые аспекты |
|---|---|---|
| 🏛️ **[Архитектура системы](architecture.md)** | Архитектурная спецификация | Чистая архитектура, принципы SOLID, фасад-оркестратор (`ReceiverFacade`), пулы потоков gRPC и потокобезопасное состояние. |
| ⚡ **[API протокола Synapse](api_reference.md)** | Спецификация gRPC и Protobuf | Сервис `HFTLink`, методы `Ping`, `LoadScenario`, `SystemControl` и потоковая передача кадров дорожного движения (`StreamTraffic`). |
| 🗺️ **[Хранилище карт и топология](map_and_topology.md)** | Загрузка дорожных сетей | Бинарная запись (`LocalMapStorage`), gzip-распаковка и парсинг светофоров SUMO (`SumoNetParser`). |
| 🖥️ **[Панель управления Tkinter](ui_and_dashboard.md)** | Интерфейс и диагностика | Темный интерфейс (`#1e1e2e`), измерение частоты пакетов (Гц), движок обнаружения нулевых данных и автоматический headless-режим. |
| 🧪 **[Тестирование и контроль качества](testing.md)** | Валидация и покрытие | Тестовый набор Pytest из 39 тестов, покрытие кода более 95%, детерминированные моки контекста gRPC и тесты многопоточности. |
| 🚀 **[Развертывание и Docker](deployment.md)** | Контейнеризация и эксплуатация | Легковесный образ Docker на базе Python 3.12-slim, `docker-compose.yml`, сокет-проверка жизнеспособности и служба Systemd. |
| 🛠️ **[Руководство разработчика](developer_guides.md)** | Расширение и поддержка | Настройка локальной среды, компиляция файлов `.proto` через `protoc`, добавление визуальных карточек и форматирование кода. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Инженерия интеллектуальной мобильности • CARINA MOCK SERVER v1.1.0</i>
</div>
