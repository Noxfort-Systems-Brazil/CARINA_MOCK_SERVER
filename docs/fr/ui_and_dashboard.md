<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🖥️ Interface Desktop Tkinter & Diagnostic Télémétrique

Ce document décrit l'interface graphique utilisateur, le thème sombre Noxfort et le moteur de diagnostic de **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [Référence API](api_reference.md) | 🧪 [Tests](testing.md)

---

## 1. Conception de l'Interface Utilisateur

L'interface de bureau est développée en **Tkinter** natif, organisée en cartes modulaires découplées sous une palette sombre opérationnelle (`ui/theme.py`).

### 1.1 Boucle de Rafraîchissement Non-Bloquante
La fenêtre principale déclenche un rafraîchissement toutes les **250 millisecondes** via `self.root.after(250, self._update_loop)` :
- Interrogation d'un `TelemetrySnapshot` immuable.
- Fluidité garantie et absence totale d'interférence sur les threads réseau gRPC.

---

## 2. Composants Visuels

1. **En-tête (`ui/components/header.py`) :** Identité visuelle et pastille d'état de connexion en direct.
2. **Carte de Connexion (`ui/components/connection_card.py`) :** Adresse gRPC, état actuel (`IDLE`, `RUNNING`) et horodatage du dernier battement de cœur.
3. **Carte de Scénario (`ui/components/scenario_card.py`) :** Nom du fichier de carte, hash SHA-256, nombre de nœuds/arêtes et taille du fichier.
4. **Carte de Flux (`ui/components/stream_card.py`) :** Nombre total de paquets, ID de séquence et fréquence mesurée en Hertz (fenêtre glissante).
5. **Carte de Diagnostic (`ui/components/diagnostics_card.py`) :** Bannière d'alerte de données (🟢 DONNÉES ACTIVES vs ⚠️ DONNÉES À ZÉRO), total des voies actives et tableau d'échantillons en direct.
6. **Carte d'Événements (`ui/components/events_card.py`) :** Journal circulaire des 15 derniers événements du serveur.

---

## 3. Mode Sans Tête (Headless)

Pour les serveurs en nuage, conteneurs Docker et environnements d'intégration continue :
```bash
python main.py --no-gui
# Ou via variable d'environnement :
MOCK_SERVER_NO_GUI=1 python main.py
```
Si Tkinter ne peut initialiser d'affichage par manque de serveur X11, le serveur bascule automatiquement en mode headless sans interruption.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guide d'Interface & Diagnostic • CARINA MOCK SERVER</i>
</div>
