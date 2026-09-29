# ⚡ Protocolo Synapse HFT: Referência da API gRPC e Estruturas Protobuf

Este documento descreve detalhadamente o contrato de interface de rede gRPC e as definições Protobuf do protocolo **Synapse HFT** implementado pelo **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](../README.md) | 🏛️ [Arquitetura](architecture.md) | 🖥️ [Interface Tkinter](ui_and_dashboard.md) | 🧪 [Testes](testing.md)

---

## 1. Visão Geral do Protocolo

O protocolo **Synapse HFT** (High-Frequency Telemetry) é a camada de comunicação de altíssima velocidade entre o ecossistema CARINA e componentes de telemetria externa, simuladores e arneses de validação.

- **Camada de Transporte:** gRPC sobre HTTP/2 com streaming binário.
- **Definição de Interface:** Protocol Buffers v3 (`proto/synapse_hft.proto`).
- **Porta Padrão:** `50051` (personalizável via variável `MOCK_SERVER_PORT`).
- **Latência Alvo:** Sub-milissegundo ($< 1\text{ ms}$) por frame transmitido.

---

## 2. Métodos do Serviço `HFTLink`

### 2.1 `Ping`
Verificação instantânea de conectividade e liveness do servidor.
- **Entrada:** `Empty`
- **Saída:** `SystemState`
  ```protobuf
  message SystemState {
    bool active = 1;        // Indica se o servidor está pronto para operações
    string state = 2;       // Estado atual: "IDLE", "READY", "RUNNING", "PAUSED"
    uint64 server_time = 3; // Timestamp do servidor em milissegundos
  }
  ```

### 2.2 `LoadScenario`
Carregamento de malha viária, definições geométricas e programações de semáforo.
- **Entrada:** `ScenarioDefinition`
  - `map_hash`: hash SHA-256 do mapa.
  - `graph`: grafo contendo nós e arestas da malha viária.
  - `geometry`: pontos poligonais para renderização.
  - `map_file_content`: bytes brutos do arquivo viário (ex.: SUMO `.net.xml` ou compactado `.gz`).
  - `map_file_name`: nome do arquivo (ex.: `londrina.net.xml.gz`).
- **Saída:** `ScenarioStatus` (`accepted`: booleano, `message`: texto de retorno).
- **Processamento:** O servidor persiste o arquivo em disco via `LocalMapStorage`, executa a extração de faixas e semáforos pelo `SumoNetParser` e atualiza o estado para `"READY"`.

### 2.3 `SystemControl`
Controle da máquina de estados do ambiente de teste.
- **Entrada:** `ControlCommand` com ações: `START`, `PAUSE`, `STOP`, `RESET`.
- **Saída:** `CommandResponse` (`success`: booleano, `new_state`: novo estado operacional).

### 2.4 `StreamTraffic`
Streaming bidirecional de alta frequência para envio contínuo de pacotes de tráfego.
- **Entrada:** Fluxo contínuo de `TrafficFrame`:
  ```protobuf
  message TrafficFrame {
    double timestamp = 1;
    uint64 sequence_id = 2;
    map<string, EdgeState> edges = 3;
  }

  message EdgeState {
    float occupancy = 1;     // Taxa de ocupação da via (0.0 a 1.0)
    float mean_speed = 2;    // Velocidade média dos veículos (m/s)
    int32 queue_length = 3;  // Número de veículos em fila
    float density = 4;       // Densidade de tráfego
  }
  ```
- **Saída:** `SystemState` (retornado no fechamento gracioso do canal de streaming).

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Referência Técnica do Protocolo Synapse • CARINA MOCK SERVER</i>
</div>
