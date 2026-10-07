<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — Suite de Documentation Technique
### Banc d'Essai de Télémétrie Haute Fréquence (HFT) et Validation du Protocole Synapse
*Noxfort Systems — A State Of Art Company*

[![Statut](https://img.shields.io/badge/Statut-Actif-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Couverture](https://img.shields.io/badge/Couverture-95.7%25-success?style=flat)](../../tests/)
[![Licence](https://img.shields.io/badge/Licence-Apache_2.0-blue?style=flat)](../../LICENSE)

---

🌐 **Langues:** **[🇺🇸 English](../en/README.md)** • **[🇧🇷 Português (Brasil)](../pt-br/README.md)** • **[🇪🇸 Español](../es/README.md)** • **[🇫🇷 Français](README.md)** • **[🇷🇺 Русский](../ru/README.md)** • **[🇨🇳 简体中文](../zh/README.md)** • **[📚 Centre de Documentation](../README.md)**

---

</div>

## Bienvenue sur la Documentation Officielle en Français

Ce répertoire rassemble l'ensemble de la documentation technique en **Français** de **CARINA MOCK SERVER** — le serveur de test et de validation de télémétrie haute fréquence (HFT) et du protocole Synapse au sein de l'écosystème de mobilité autonome de Noxfort Systems.

Conçu selon les principes de l'**Architecture Propre** et de **SOLID**, il sert de puits de télémétrie et d'environnement d'étalonnage pour les agents de contrôle de feux tricolores par apprentissage par renforcement profond, les jumeaux numériques et les passerelles de terrain.

---

## 📚 Guides Techniques Spécialisés

| Document | Domaine & Portée | Points Clés |
|---|---|---|
| 🏛️ **[Architecture du Système](architecture.md)** | Spécification d'Architecture | Architecture propre, principes SOLID, façade d'orchestration (`ReceiverFacade`), concurrence multithread et état thread-safe. |
| ⚡ **[API du Protocole Synapse](api_reference.md)** | Spécification gRPC & Protobuf | Service `HFTLink`, méthodes `Ping`, `LoadScenario`, `SystemControl` et diffusion continue de trames de trafic (`StreamTraffic`). |
| 🗺️ **[Stockage & Topologie SUMO](map_and_topology.md)** | Ingestion Réseau Routier | Persistance binaire (`LocalMapStorage`), décompression gzip et analyse des carrefours à feux (`SumoNetParser`). |
| 🖥️ **[Tableau de Bord Tkinter & Diagnostic](ui_and_dashboard.md)** | Interface & Télémétrie | Tableau de bord de bureau sombre (`#1e1e2e`), mesure de fréquence (Hz), moteur de détection de trames à zéro et mode sans tête (headless). |
| 🧪 **[Tests & Assurance Qualité](testing.md)** | Validation & Couverture | Suite Pytest comprenant 39 tests automatisés, couverture supérieure à 95%, simulations de contexte gRPC et tests de concurrence. |
| 🚀 **[Déploiement & Conteneurs](deployment.md)** | Docker & Exploitation | Image Docker basée sur Python 3.12-slim, `docker-compose.yml`, vérifications de santé par socket, variables d'environnement et unité Systemd. |
| 🛠️ **[Guide du Développeur](developer_guides.md)** | Extension & Maintenance | Configuration de l'environnement local, compilation `.proto` avec `protoc`, création de cartes graphiques et normes de journalisation. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Ingénierie de Mobilité Intelligente • CARINA MOCK SERVER v1.1.0</i>
</div>
