<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🏛️ CARINA MOCK SERVER: Arquitectura del Sistema y Principios de Ingeniería

Este documento detalla la arquitectura técnica interna de **CARINA MOCK SERVER**: capas de Arquitectura Limpia, principios SOLID, ciclo de vida de los componentes, modelo de concurrencia y motor de diagnóstico de datos en tiempo real.

⬅️ [Centro de Documentación](../README.md) | ⚡ [Referencia de la API](api_reference.md) | 🖥️ [Panel Tkinter](ui_and_dashboard.md) | 🧪 [Pruebas](testing.md)

---

## 1. Principios Arquitectónicos y Diseño en Capas

CARINA MOCK SERVER aplica rigurosamente los principios **SOLID**:

1. **Responsabilidad Única (SRP):** Cada módulo gestiona un único propósito:
   - `SumoNetParser`: interpreta la topología XML y semáforos de SUMO.
   - `LocalMapStorage`: gestiona el almacenamiento y descompresión de mapas binarios.
   - `TelemetryState`: mantiene el estado thread-safe y el histórico de eventos.
2. **Abierto/Cerrado (OCP):** Nuevos motores de registro o persistencia se integran mediante interfaces de `src/core/interfaces.py` sin alterar el núcleo.
3. **Sustitución de Liskov (LSP):** Todos los loggers (`ConsoleLogger`, `FileLogger`, `CompositeLogger`) implementan `ILogger` de manera intercambiable.
4. **Segregación de Interfaces (ISP):** Clientes acceden a contratos especializados:
   - `ITelemetryCollector`: métodos de escritura para gRPC.
   - `ITelemetryProvider`: consultas de sólo lectura para la interfaz gráfica.
5. **Inversión de Dependencias (DIP):** Los servicios de alto nivel (`HFTService`, `ReceiverFacade`) dependen de abstracciones, nunca de clases concretas de infraestructura.

---

## 2. Jerarquía de Componentes y Flujo de Datos

```mermaid
graph TD
    CLI[main.py / CLI] -->|Instancia| Facade[ReceiverFacade]
    
    subgraph Capa Core ["Capa Core (Abstracciones y Estado)"]
        Interfaces[src/core/interfaces.py]
        Config[src/core/config.py]
        State[src/core/telemetry_state.py]
    end

    subgraph Capa de Aplicación ["Capa de Aplicación (Protocolos)"]
        HFT[src/application/hft_service.py]
    end

    subgraph Capa de Infraestructura ["Capa de Infraestructura (E/S y Red)"]
        GRPC[src/infrastructure/grpc_server.py]
        Storage[src/infrastructure/map_storage.py]
        Parser[src/infrastructure/sumo_parser.py]
        Loggers[src/infrastructure/composite_logger.py]
    end

    subgraph Capa de Presentación ["Capa de Presentación (GUI)"]
        UI[ui/dashboard.py]
        Cards[ui/components/*]
    end

    Facade --> Capa Core
    Facade --> Capa de Aplicación
    Facade --> Capa de Infraestructura
    Facade --> Capa de Presentación

    GRPC -->|Despacha RPCs| HFT
    HFT -->|Registra Métricas| State
    HFT -->|Guarda Mapa| Storage
    HFT -->|Extrae Topología| Parser
    UI -->|Consulta Snapshot| State
```

---

## 3. Concurrencia y Sincronización Segura

- **Pool de Hilos gRPC:** `GrpcServer` asigna un `ThreadPoolExecutor(max_workers=10)` para procesar flujos de telemetria sin bloquear la red.
- **Aislamiento con Cerrojo Exclusivo:** `TelemetryState` protege todos sus datos mutables mediante `threading.Lock()`.
- **Snapshots Inmutables:** El hilo de Tkinter consulta `get_snapshot()` cada 250 ms, obteniendo un dataclass inmutable sin contención sobre los hilos de red.
- **Apagado Ordenado:** `ReceiverFacade` intercepta señales de terminación (`SIGINT`, `SIGTERM`), cerrando ordenadamente sockets y archivos de registro.

---

## 4. Motor de Detección de Datos en Cero

En la validación de control semafórico mediante IA, los paquetes con valores en cero (ocupación = 0, velocidad = 0, cola = 0 en toda la red) indican fallos silenciosos de recolección en los sensores.

El motor de diagnóstico evalúa cada trama entrante:
- Se evalúa cada vía frente al umbral $\epsilon = 10^{-4}$.
- Si no hay vías activas, se activa la alerta `all_zeros = True`, reflejada de inmediato en el panel visual y en los registros de log.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Especificación Arquitectónica • CARINA MOCK SERVER</i>
</div>
