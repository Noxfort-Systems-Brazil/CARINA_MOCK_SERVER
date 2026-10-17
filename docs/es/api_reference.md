<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# ⚡ Protocolo Synapse HFT: Referencia de API gRPC y Protobuf

Este documento describe detalladamente la especificación de red gRPC y los mensajes Protocol Buffers del protocolo **Synapse HFT** en **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](../README.md) | 🏛️ [Arquitectura](architecture.md) | 🖥️ [Panel Tkinter](ui_and_dashboard.md) | 🧪 [Pruebas](testing.md)

---

## 1. Visión General del Protocolo

El protocolo **Synapse HFT** proporciona la interfaz de telemetría de ultra baja latencia entre el controlador de tráfico de CARINA y los servidores de prueba o gemelos digitales.

- **Transporte:** HTTP/2 mediante gRPC con transmisión binaria.
- **Definición:** Protocol Buffers v3 (`proto/synapse_hft.proto`).
- **Puerto:** `50051` (configurable mediante `MOCK_SERVER_PORT`).
- **Latencia Objetivo:** Sub-milisegundo ($< 1\text{ ms}$).

---

## 2. Métodos del Servicio `HFTLink`

### 2.1 `Ping`
Comprobación de conectividad y estado operativo del servidor.
- **Entrada:** `Empty`
- **Salida:** `SystemState` (`active`, `state`, `server_time`).

### 2.2 `LoadScenario`
Carga de topología de red, geometría y archivos de mapa.
- **Entrada:** `ScenarioDefinition` (hash, grafo de nodos/aristas, geometría, contenido binario del archivo `.net.xml`/`.gz`).
- **Salida:** `ScenarioStatus` (`accepted`, `message`).
- **Comportamiento:** Persiste el mapa en disco, ejecuta `SumoNetParser` para extraer carriles y semáforos, y actualiza el estado a `"READY"`.

### 2.3 `SystemControl`
Control de la máquina de estados de simulación.
- **Entrada:** `ControlCommand` (`START`, `PAUSE`, `STOP`, `RESET`).
- **Salida:** `CommandResponse` (`success`, `new_state`).

### 2.4 `StreamTraffic`
Transmisión continua bidireccional de paquetes de telemetría de tráfico.
- **Entrada:** Flujo de `TrafficFrame`:
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }
  ```
- **Salida:** `SystemState` al cerrar la conexión.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Referencia de API Synapse • CARINA MOCK SERVER</i>
</div>
