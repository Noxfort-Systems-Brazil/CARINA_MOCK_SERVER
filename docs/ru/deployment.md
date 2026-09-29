# 🚀 Развертывание, контейнеризация и эксплуатация

Данный документ описывает развертывание в контейнерах Docker, оркестрацию с Docker Compose и работу без графической подсистемы для **CARINA MOCK SERVER**.

⬅️ [Главный Хаб Документации](../README.md) | 🏛️ [Архитектура](architecture.md) | ⚡ [Спецификация API](api_reference.md) | 🧪 [Тестирование](testing.md)

---

## 1. Контейнеризация с Docker

В репозитории подготовлен `Dockerfile` на базе официального образа `python:3.12-slim`:
- Малый объем образа (< 150 МБ).
- Запуск по умолчанию в headless-режиме (`--no-gui`).
- Встроенный механизм контроля здоровья (Healthcheck) на порту `50051`.

### 1.1 Сборка и запуск контейнера
```bash
docker build -t carina-mock-server:latest .
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  carina-mock-server:latest
```

---

## 2. Docker Compose

```bash
docker compose up -d --build
docker compose logs -f
docker compose down
```

---

## 3. Переменные окружения

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | Сетевой адрес интерфейса для сокета gRPC. |
| `MOCK_SERVER_PORT` | `50051` | Порт входящих соединений протокола Synapse HFT. |
| `MOCK_SERVER_NO_GUI` | `1` (в контейнерах) | Отключение Tkinter и работа в headless-режиме. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Руководство по развертыванию • CARINA MOCK SERVER</i>
</div>
