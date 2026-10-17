<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — Suite de Documentación Técnica
### Arnés de Pruebas de Alta Frecuencia (HFT) y Validación del Protocolo Synapse
*Noxfort Systems — A State Of Art Company*

[![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Cobertura](https://img.shields.io/badge/Cobertura-95.7%25-success?style=flat)](../../tests/)
[![SPDX-License-Identifier](https://img.shields.io/badge/SPDX--License--Identifier-Apache--2.0-blue?style=flat)](../../LICENSE)

---

🌐 **Idiomas:** **[🇺🇸 English](../en/README.md)** • **[🇧🇷 Português (Brasil)](../pt-br/README.md)** • **[🇪🇸 Español](README.md)** • **[🇫🇷 Français](../fr/README.md)** • **[🇷🇺 Русский](../ru/README.md)** • **[🇨🇳 简体中文](../zh/README.md)** • **[📚 Centro de Documentación](../README.md)**

---

</div>

## Bienvenido a la Documentación Oficial en Español

Este directorio reúne la suite completa de documentación técnica en **Español** de **CARINA MOCK SERVER** — el servidor oficial de pruebas y validación de telemetría de alta frecuencia (HFT) y protocolo Synapse del ecosistema de movilidad inteligente de Noxfort Systems.

Diseñado bajo los principios de **Arquitectura Limpia** y **SOLID**, actúa como banco de pruebas y servidor de validación para agentes de aprendizaje por refuerzo profundo, gemelos digitales y pasarelas de hardware.

---

## 📚 Índice de Guías Técnicas

| Documento | Tema y Alcance | Aspectos Destacados |
|---|---|---|
| 🏛️ **[Arquitectura del Sistema](architecture.md)** | Especificación Arquitectónica | Arquitectura limpia, principios SOLID, fachada orquestadora (`ReceiverFacade`), concurrencia multihilo y estado thread-safe. |
| ⚡ **[API del Protocolo Synapse](api_reference.md)** | Especificación gRPC y Protobuf | Servicio `HFTLink`, llamadas `Ping`, `LoadScenario`, `SystemControl` y transmisión continua de tramas de tráfico (`StreamTraffic`). |
| 🗺️ **[Almacenamiento y Topología](map_and_topology.md)** | Ingestión de Redes Viales | Persistencia binaria (`LocalMapStorage`), descompresión gzip y análisis de semáforos (`SumoNetParser`). |
| 🖥️ **[Panel Tkinter y Diagnóstico](ui_and_dashboard.md)** | Interfaz y Telemetría | Panel de escritorio oscuro (`#1e1e2e`), medición de frecuencia (Hz), motor de detección de datos en cero y modo sin interfaz (headless). |
| 🧪 **[Pruebas y Control de Calidad](testing.md)** | Validación y Cobertura | Suite Pytest con 39 pruebas automatizadas, cobertura superior al 95%, mocks deterministas de gRPC y pruebas de concurrencia. |
| 🚀 **[Despliegue y Contenedores](deployment.md)** | Docker y Operaciones | Imagen Docker basada en Python 3.12-slim, `docker-compose.yml`, health checks de socket, variables de entorno y servicio Systemd. |
| 🛠️ **[Guías de Desarrollo](developer_guides.md)** | Extensión y Mantenimiento | Entorno local, compilación de archivos `.proto` con `protoc`, creación de nuevas tarjetas visuales y estándares de registro. |

## 📄 Licencia y Conformidad SPDX

Este proyecto y su documentación técnica están licenciados bajo la [Apache License 2.0](../../LICENSE).

- **SPDX-License-Identifier:** `Apache-2.0`
- **SPDX-FileCopyrightText:** `2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>`

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Ingeniería de Movilidad Inteligente • CARINA MOCK SERVER v1.1.0</i><br/>
  <small>SPDX-License-Identifier: <a href="../../LICENSE">Apache-2.0</a> • SPDX-FileCopyrightText: © 2026 Noxfort Systems.</small>
</div>
