<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🏛️ CARINA MOCK SERVER: Blueprint de Arquitetura e Engenharia de Software

Este documento especifica a arquitetura interna do **CARINA MOCK SERVER**: seus padrões de Arquitetura Limpa, princípios SOLID, ciclo de vida dos subsistemas, modelo de concorrência multithread e o motor de diagnóstico de dados em tempo real.

⬅️ [Central de Documentação](../README.md) | ⚡ [Referência da API](api_reference.md) | 🖥️ [Interface Tkinter](ui_and_dashboard.md) | 🧪 [Testes](testing.md)

---

## 1. Princípios Arquiteturais e Design em Camadas

O CARINA MOCK SERVER foi projetado com estrita aderência aos princípios **SOLID** e separação limpa de responsabilidades:

1. **Responsabilidade Única (SRP):** Cada componente resolve um domínio isolado:
   - `SumoNetParser`: restrito à interpretação do XML de malha viária e semáforos.
   - `LocalMapStorage`: manipulação de arquivos binários e compressão `.gz` em disco.
   - `TelemetryState`: gerenciamento thread-safe do estado interno de métricas e histórico.
2. **Aberto/Fechado (OCP):** Novos mecanismos de armazenamento ou visualizadores podem ser plugados através das interfaces de `src/core/interfaces.py` sem alteração no núcleo do servidor.
3. **Substituição de Liskov (LSP):** Os diferentes registradores (`ConsoleLogger`, `FileLogger`, `CompositeLogger`) implementam a abstração `ILogger` de forma totalmente intercambiável.
4. **Segregação de Interfaces (ISP):** Os clientes acessam apenas contratos especializados:
   - `ITelemetryCollector`: expõe métodos de escrita utilizados pelo manipulador gRPC.
   - `ITelemetryProvider`: expõe métodos somente-leitura consumidos pela interface gráfica.
5. **Inversão de Dependência (DIP):** Os serviços de alto nível (`HFTService`, `ReceiverFacade`) dependem exclusivamente de interfaces abstratas, jamais de implementações concretas de infraestrutura.

---

## 2. Visão Geral dos Componentes e Camadas

```mermaid
graph TD
    CLI[main.py / Argumentos de Linha de Comando] -->|Instancia| Facade[ReceiverFacade]
    
    subgraph Camada Core ["Camada Core (Domínio e Interfaces)"]
        Interfaces[src/core/interfaces.py]
        Config[src/core/config.py]
        State[src/core/telemetry_state.py<br/>ITelemetryCollector & ITelemetryProvider]
    end

    subgraph Camada de Aplicação ["Camada de Aplicação (Serviços e Protocolo)"]
        HFT[src/application/hft_service.py<br/>HFTLinkServicer]
    end

    subgraph Camada de Infraestrutura ["Camada de Infraestrutura (E/S e Rede)"]
        GRPC[src/infrastructure/grpc_server.py]
        Storage[src/infrastructure/map_storage.py]
        Parser[src/infrastructure/sumo_parser.py]
        Loggers[src/infrastructure/composite_logger.py<br/>ConsoleLogger & FileLogger]
    end

    subgraph Camada de Apresentação ["Camada de Apresentação (GUI)"]
        UI[ui/dashboard.py<br/>TkinterDashboard]
        Cards[ui/components/*<br/>Cards Modulares]
    end

    Facade --> Camada Core
    Facade --> Camada de Aplicação
    Facade --> Camada de Infraestrutura
    Facade --> Camada de Apresentação

    GRPC -->|Despacha RPCs| HFT
    HFT -->|Grava Métricas| State
    HFT -->|Persiste Mapa| Storage
    HFT -->|Processa Topologia| Parser
    UI -->|Lê Snapshot Imutável| State
```

---

## 3. Modelo de Concorrência e Segurança de Threads

- **Pool de Threads gRPC:** O `GrpcServer` aloca um pool de execução concorrente (`ThreadPoolExecutor(max_workers=10)`), permitindo o atendimento instantâneo a conexões concorrentes de telemetria sem bloqueio de I/O.
- **Isolamento de Estado com Trava Exclusiva:** O objeto `TelemetryState` protege todas as suas variáveis mutáveis (frequência de frames, detecção de zeros, lista de amostras e histórico) por meio de um `threading.Lock()`.
- **Snapshots Imutáveis para a Interface:** Para evitar contenção de trava na interface gráfica, o método `get_snapshot()` constrói um dataclass imutável (`TelemetrySnapshot`) dentro da seção crítica e o devolve à thread principal do Tkinter, garantindo renderização sem travas.
- **Encerramento Idempotente e Tratamento de Sinais:** Sinais do sistema operacional (`SIGINT` e `SIGTERM`) são interceptados de forma segura pelo `ReceiverFacade`, coordenando o encerramento gracioso do servidor de rede e a liberação de recursos de arquivos.

---

## 4. Motor de Diagnóstico de Dados Zerados

Em pipelines de Aprendizado por Reforço para controle de tráfego, pacotes contendo apenas valores zerados (ocupação = 0, velocidade = 0 e fila = 0 em todas as faixas) representam falhas silenciosas de coleta de dados no simulador ou agente.

O motor do CARINA MOCK SERVER avalia cada frame recebido:
- Cada aresta é confrontada com o limiar $\epsilon = 10^{-4}$.
- Se nenhuma aresta apresentar valor positivo, o frame é catalogado como `all_zeros = True`, disparando alerta visual na UI e registro de aviso nos arquivos de log.
- O sistema retém em memória até 5 amostras ativas e 3 amostras zeradas para inspeção forense instantânea no painel.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Especificação Arquitetural • CARINA MOCK SERVER</i>
</div>
