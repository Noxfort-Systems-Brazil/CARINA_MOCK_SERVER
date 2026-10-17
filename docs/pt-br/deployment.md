<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# 🚀 Deploy, Conteinerização e Operação em Servidores

Este documento descreve os procedimentos de empacotamento em contêineres Docker, orquestração com Docker Compose e execução em segundo plano para o **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](../README.md) | 🏛️ [Arquitetura](architecture.md) | ⚡ [Referência da API](api_reference.md) | 🧪 [Testes](testing.md)

---

## 1. Conteinerização com Docker

O servidor possui um `Dockerfile` otimizado em múltiplos estágios baseado na imagem oficial `python:3.12-slim`:
- Imagem leve com tamanho inferior a 150 MB.
- Configuração padrão para execução headless (`--no-gui`).
- Verificação periódica de saúde (Healthcheck) por checagem de socket na porta `50051`.

### 1.1 Comandos de Construção e Execução
```bash
# Construção da imagem Docker
docker build -t carina-mock-server:latest .

# Execução do contêiner expondo a porta de telemetria
docker run -d \
  --name carina-mock-server \
  -p 50051:50051 \
  -v $(pwd)/data/maps:/app/data/maps \
  carina-mock-server:latest
```

---

## 2. Orquestração com Docker Compose

O repositório disponibiliza arquivo `docker-compose.yml` para implantação em um único comando:

```bash
# Inicialização dos serviços em segundo plano
docker compose up -d --build

# Acompanhamento dos logs em tempo real
docker compose logs -f

# Encerramento do contêiner
docker compose down
```

---

## 3. Variáveis de Ambiente

| Variável | Valor Padrão | Descrição |
|---|---|---|
| `MOCK_SERVER_HOST` | `0.0.0.0` / `[::]` | Interface de rede para vinculação do socket gRPC. |
| `MOCK_SERVER_PORT` | `50051` | Porta de escuta para as mensagens Synapse HFT. |
| `MOCK_SERVER_NO_GUI` | `1` (em contêineres) | Desativa a interface Tkinter e ativa o loop headless. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guia de Implantação e Deploy • CARINA MOCK SERVER</i>
</div>
