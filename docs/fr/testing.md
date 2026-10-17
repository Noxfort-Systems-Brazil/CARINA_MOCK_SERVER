<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🧪 Stratégie de Tests & Assurance Qualité

Ce document décrit la suite de tests automatisés, les exigences de couverture et les procédures de validation de **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [Référence API](api_reference.md) | 🚀 [Déploiement](deployment.md)

---

## 1. Normes de Qualité & Couverture

- **Exécuteur de Tests :** `pytest` avec l'extension `pytest-cov`.
- **Seuil Minimal Requis :** **80%** (appliqué via `--cov-fail-under=80`).
- **Couverture Atteinte :** **95,7%** sur l'ensemble des modules sous `src/`.
- **Total de Tests :** 39 tests unitaires et d'intégration s'exécutant en moins d'une seconde.

---

## 2. Structure des Tests (`tests/`)

- `test_config.py` : Ports par défaut et substitution par variables d'environnement.
- `test_grpc_server.py` : Gestion du cycle de vie du serveur réseau et requêtes ping.
- `test_hft_service.py` : RPCs de contrôle, chargement de cartes, streaming continu et gestion des erreurs.
- `test_loggers.py` : Validation des sorties console, fichiers rotatifs et composite.
- `test_map_storage.py` : Sauvegarde binaire des réseaux, extensions automatiques et résilience aux pannes disque.
- `test_receiver_facade.py` : Initialisation de l'orchestrateur et basculement headless automatique.
- `test_sumo_parser.py` : Analyse syntaxique XML des réseaux SUMO et gestion des fichiers corrompus.
- `test_telemetry_state.py` : Concurrence multithread, calcul de débit en Hz, détection de données à zéro et expiration de session.

---

## 3. Commandes d'Exécution

```bash
# Exécution complète avec rapport de couverture
pytest

# Exécution ciblée d'un module
pytest tests/test_hft_service.py -v

# Génération d'un rapport visuel HTML
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Assurance Qualité & Tests • CARINA MOCK SERVER</i>
</div>
