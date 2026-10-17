<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🏛️ CARINA MOCK SERVER: Architecture du Système et Conception Logicielle

Ce document détaille l'architecture interne de **CARINA MOCK SERVER** : couches d'Architecture Propre, principes SOLID, cycle de vie des sous-systèmes, modèle de concurrence et moteur de diagnostic en temps réel.

⬅️ [Centre de Documentation](../README.md) | ⚡ [Référence API](api_reference.md) | 🖥️ [Tableau de Bord Tkinter](ui_and_dashboard.md) | 🧪 [Tests](testing.md)

---

## 1. Principes d'Architecture & SOLID

CARINA MOCK SERVER applique rigoureusement les principes de l'**Architecture Propre** et de **SOLID** :

1. **Responsabilité Unique (SRP) :** Chaque module répond à une préoccupation isolée :
   - `SumoNetParser` : analyse des fichiers XML de réseaux routiers et carrefours à feux.
   - `LocalMapStorage` : persistance sur disque et décompression des cartes gzip.
   - `TelemetryState` : gestion de l'état thread-safe et historique des événements.
2. **Ouvert/Fermé (OCP) :** De nouveaux mécanismes de stockage ou de journalisation peuvent être connectés via `src/core/interfaces.py` sans impacter l'orchestrateur.
3. **Substitution de Liskov (LSP) :** Tous les enregistreurs (`ConsoleLogger`, `FileLogger`, `CompositeLogger`) implémentent `ILogger` de manière transparente.
4. **Ségrégation des Interfaces (ISP) :** Séparation nette entre :
   - `ITelemetryCollector` : méthodes d'écriture destinées au gestionnaire gRPC.
   - `ITelemetryProvider` : requêtes de lecture consommées par l'interface graphique.
5. **Inversion des Dépendances (DIP) :** Les composants de haut niveau (`HFTService`, `ReceiverFacade`) reposent sur des abstractions plutôt que des classes concrètes.

---

## 2. Hiérarchie des Composants & Flux de Données

```mermaid
graph TD
    CLI[main.py / CLI] -->|Instancie| Facade[ReceiverFacade]
    
    subgraph Couche Core ["Couche Core (Domaine & Abstractions)"]
        Interfaces[src/core/interfaces.py]
        Config[src/core/config.py]
        State[src/core/telemetry_state.py]
    end

    subgraph Couche Application ["Couche Application (Protocoles)"]
        HFT[src/application/hft_service.py]
    end

    subgraph Couche Infrastructure ["Couche Infrastructure (E/S & Réseau)"]
        GRPC[src/infrastructure/grpc_server.py]
        Storage[src/infrastructure/map_storage.py]
        Parser[src/infrastructure/sumo_parser.py]
        Loggers[src/infrastructure/composite_logger.py]
    end

    subgraph Couche Présentation ["Couche Présentation (GUI)"]
        UI[ui/dashboard.py]
        Cards[ui/components/*]
    end

    Facade --> Couche Core
    Facade --> Couche Application
    Facade --> Couche Infrastructure
    Facade --> Couche Présentation

    GRPC -->|Transmet RPCs| HFT
    HFT -->|Enregistre Métriques| State
    HFT -->|Sauvegarde Carte| Storage
    HFT -->|Extrait Topologie| Parser
    UI -->|Lit Snapshot Immuable| State
```

---

## 3. Concurrence & Synchronisation Multithread

- **Pool de Threads gRPC :** `GrpcServer` gère un `ThreadPoolExecutor(max_workers=10)` pour traiter les flux sans bloquer le réseau.
- **Section Critique Isolée :** `TelemetryState` protège ses variables mutables via un verrou exclusif `threading.Lock()`.
- **Instantanés Immuables pour l'Interface :** Le thread Tkinter interroge `get_snapshot()` toutes les 250 ms, recevant un dataclass immuable sans bloquer les threads de diffusion gRPC.
- **Arrêt Propre :** `ReceiverFacade` capture les signaux système (`SIGINT`, `SIGTERM`), fermant les canaux réseau et libérant les descripteurs de fichiers.

---

## 4. Moteur de Détection de Données à Zéro

Dans le contrôle de trafic urbain par IA, des trames ne contenant que des zéros (taux d'occupation = 0, vitesse = 0, file d'attente = 0 sur l'ensemble des voies) signalent des anomalies critiques de collecte de données.

Le moteur de diagnostic évalue chaque trame reçue :
- Chaque voie est comparée au seuil $\epsilon = 10^{-4}$.
- Si aucune voie active n'est détectée, `all_zeros` passe à `True`, affichant une alerte visuelle et émettant un avertissement dans les logs.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Spécification d'Architecture • CARINA MOCK SERVER</i>
</div>
