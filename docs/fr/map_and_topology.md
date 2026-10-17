<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🗺️ Stockage des Cartes & Analyseur de Topologie SUMO

Ce document spécifie le sous-système de persistance et d'analyse de réseaux routiers SUMO au sein de **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [Référence API](api_reference.md) | 🖥️ [Tableau de Bord Tkinter](ui_and_dashboard.md)

---

## 1. Rôle du Sous-Système

Les réseaux routiers urbains de CARINA sont modélisés au format Eclipse SUMO (`.net.xml`). Lors de l'initialisation des tests, le client transmet la carte complète via la méthode gRPC `LoadScenario`.

Le traitement repose sur deux modules découplés :
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`) :** Persistance binaire sur disque et normalisation des extensions (`.net.xml`, `.net.xml.gz`).
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`) :** Analyse syntaxique via `sumolib`, extraction des voies et détection des régulateurs de carrefour (`<tlLogic>`).

---

## 2. Stockage Binaire (`LocalMapStorage`)

Implémente `IMapStorage` (`src/core/interfaces.py`) :
- **Répertoire :** `data/maps/` (créé automatiquement).
- **Gestion des Extensions :** Ajoute `.net.xml` si absente et gère les fichiers compressés `.gz`.
- **Écriture Sécurisée :** Écriture directe des flux d'octets bruts.

---

## 3. Analyseur de Topologie (`SumoNetParser`)

Implémente `IMapParser` :
1. **Géométrie des Voies :** Parcours des arêtes et voies pour extraire les coordonnées polylignes (`lane.getShape()`).
2. **Feux Tricolores :** Extraction des coordonnées et identifiants des nœuds contrôlés.
3. **Résilience :** Gestion des absences de dépendance `sumolib` sans interruption de service.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guide de Stockage & Topologie • CARINA MOCK SERVER</i>
</div>
