# 🚀 Déploiement, Conteneurs Docker & Exploitation

Ce document décrit l'empaquetage Docker, l'orchestration Docker Compose et l'exploitation headless de **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [Référence API](api_reference.md) | 🧪 [Tests](testing.md)

---

## 1. Conteneurisation Docker

Le serveur intègre un `Dockerfile` basé sur `python:3.12-slim` :
- Empreinte réduite (< 150 Mo).
- Exécution par défaut en mode headless (`--no-gui`).
- Bilan de santé (Healthcheck) intégré par sonde de socket sur le port `50051`.

### 1.1 Commandes Docker
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

## 3. Variables d'Environnement

| Variable | Valeur par Défaut | Description |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | Interface réseau d'écoute gRPC. |
| `MOCK_SERVER_PORT` | `50051` | Port d'écoute pour la télémétrie Synapse HFT. |
| `MOCK_SERVER_NO_GUI` | `1` (dans les conteneurs) | Désactive l'interface graphique et active le mode sans tête. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guide de Déploiement • CARINA MOCK SERVER</i>
</div>
