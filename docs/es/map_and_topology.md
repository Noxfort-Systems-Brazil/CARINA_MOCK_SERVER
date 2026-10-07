# 🗺️ Almacenamiento de Mapas y Analizador de Topología SUMO

Este documento especifica el subsistema de almacenamiento de mapas y análisis de topología vial SUMO en **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](README.md) | 🏛️ [Arquitectura](architecture.md) | ⚡ [Referencia de la API](api_reference.md) | 🖥️ [Panel Tkinter](ui_and_dashboard.md)

---

## 1. Visión General del Subsistema

En el ecosistema CARINA, las redes viales urbanas se modelan en formato Eclipse SUMO (`.net.xml`). Durante las pruebas, los clientes transmiten la topología al servidor mediante la llamada gRPC `LoadScenario`.

El subsistema se compone de:
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`):** Gestiona la persistencia binaria en disco y normaliza extensiones de archivo (`.net.xml`, `.net.xml.gz`).
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`):** Analiza el XML vial mediante `sumolib`, extrayendo geometrías de carriles y semáforos (`<tlLogic>`).

---

## 2. Almacenamiento en Disco (`LocalMapStorage`)

Implementa `IMapStorage` (`src/core/interfaces.py`):
- **Directorio:** `data/maps/` (creado automáticamente).
- **Normalización:** Asigna la extensión `.net.xml` si falta; respeta archivos comprimidos `.gz`.
- **Escritura Segura:** Grabación directa de flujos de bytes en disco.

---

## 3. Analizador de Topología (`SumoNetParser`)

Implementa `IMapParser`:
1. **Geometría de Carriles:** Recorre aristas y carriles para extraer polilíneas vectoriales (`lane.getShape()`).
2. **Semáforos:** Filtra nodos de tipo `"traffic_light"`, obteniendo sus coordenadas `(x, y)` e identificador.
3. **Tolerancia a Fallos:** Captura excepciones si `sumolib` no está disponible, registrando una advertencia sin interrumpir el servicio gRPC.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guía de Almacenamiento y Topología • CARINA MOCK SERVER</i>
</div>
