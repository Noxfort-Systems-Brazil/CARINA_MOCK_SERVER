<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🖥️ Interface Desktop Tkinter & Diagnósticos de Telemetria

Este documento apresenta a arquitetura da interface gráfica, a paleta visual escura e o motor de diagnósticos do **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](../README.md) | 🏛️ [Arquitetura](architecture.md) | ⚡ [Referência da API](api_reference.md) | 🧪 [Testes](testing.md)

---

## 1. Arquitetura da Interface Visual

A interface do CARINA MOCK SERVER foi desenvolvida utilizando a biblioteca nativa **Tkinter**, estruturada em um padrão desacoplado orientado a cartões modulares sob o tema escuro Noxfort (`ui/theme.py`).

### 1.1 Ciclo de Atualização Não-Bloqueante
A janela principal agenda ciclos de consulta periódicos a cada **250 milissegundos** via `self.root.after(250, self._update_loop)`:
- A interface obtém uma cópia imutável `TelemetrySnapshot` da camada de dados (`TelemetryState`).
- Nenhum bloqueio de rede ou escrita ocorre na thread principal de renderização.

---

## 2. Cartões e Componentes da Interface

1. **Header (`ui/components/header.py`):** Apresenta o título do sistema e uma pílula visual indicativa de conexão ativa ou inativa.
2. **Card de Conexão (`ui/components/connection_card.py`):** Exibe o endereço IP/Porta do servidor gRPC, o estado atual (`IDLE`, `RUNNING`) e o tempo decorrido desde o último heartbeat.
3. **Card de Cenário (`ui/components/scenario_card.py`):** Apresenta o nome do arquivo de malha viária carregado, hash de integridade, contagem de nós/arestas e tamanho do arquivo.
4. **Card de Fluxo (`ui/components/stream_card.py`):** Exibe o contador total de frames, ID de sequência e vazão instantânea em Hertz calculada por janela deslizante de 20 amostras.
5. **Card de Diagnósticos (`ui/components/diagnostics_card.py`):** Motor de detecção de dados zerados com faixa de alerta (🟢 DADOS ATIVOS vs ⚠️ DADOS ZERADOS), contagem de vias com tráfego e tabela de inspeção em tempo real das faixas.
6. **Card de Eventos (`ui/components/events_card.py`):** Log visual circular com os 15 eventos mais recentes do servidor.

---

## 3. Modo Headless (Sem Interface Gráfica)

Para ambientes conteinerizados, servidores remotos sem servidor X11 ou pipelines de CI/CD:
```bash
# Execução via parâmetro CLI
python main.py --no-gui

# Execução via variável de ambiente
MOCK_SERVER_NO_GUI=1 python main.py
```
Caso a inicialização do Tkinter falhe por ausência de display, o sistema efetua fallback automático para o modo headless.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guia de Interface e Diagnósticos • CARINA MOCK SERVER</i>
</div>
