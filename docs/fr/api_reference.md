# ⚡ Protocole Synapse HFT: Référence API gRPC & Protobuf

Ce document spécifie le contrat d'interface réseau gRPC et les définitions Protocol Buffers du protocole **Synapse HFT** pour **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](../README.md) | 🏛️ [Architecture](architecture.md) | 🖥️ [Tableau de Bord Tkinter](ui_and_dashboard.md) | 🧪 [Tests](testing.md)

---

## 1. Vue d'Ensemble du Protocole

Le protocole **Synapse HFT** (High-Frequency Telemetry) fournit la couche de communication haute performance entre les contrôleurs d'intersection CARINA et les serveurs d'étalonnage ou simulateurs.

- **Transport :** HTTP/2 via gRPC.
- **Sérialisation :** Protocol Buffers v3 (`proto/synapse_hft.proto`).
- **Port d'Écoute :** `50051` (configurable via `MOCK_SERVER_PORT`).
- **Objectif de Latence :** Inférieure à 1 milliseconde par trame.

---

## 2. Méthodes du Service `HFTLink`

### 2.1 `Ping`
Contrôle instantané de la disponibilité du serveur.
- **Requête :** `Empty`
- **Réponse :** `SystemState` (`active`, `state`, `server_time`).

### 2.2 `LoadScenario`
Transfert de topologie routière, géométrie vectorielle et horaires de pointe.
- **Requête :** `ScenarioDefinition` (hash, graphe des nœuds/voies, géométrie, fichier binaire SUMO `.net.xml`/`.gz`).
- **Réponse :** `ScenarioStatus` (`accepted`, `message`).
- **Traitement :** Sauvegarde du fichier sur disque, extraction des voies et régulateurs (`<tlLogic>`) via `SumoNetParser`, et passage à l'état `"READY"`.

### 2.3 `SystemControl`
Contrôle de la machine à états de simulation.
- **Requête :** `ControlCommand` (`START`, `PAUSE`, `STOP`, `RESET`).
- **Réponse :** `CommandResponse` (`success`, `new_state`).

### 2.4 `StreamTraffic`
Flux continu bidirectionnel de télémétrie de trafic à haute fréquence.
- **Requête :** Flux continu de `TrafficFrame`:
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }
  ```
- **Réponse :** `SystemState` à la clôture du canal.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Référence Technique Synapse • CARINA MOCK SERVER</i>
</div>
