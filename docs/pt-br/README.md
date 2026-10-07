<div align="center">

<img src="../assets/carina-logo.png" alt="CARINA MOCK SERVER Logo" width="120" />

# CARINA MOCK SERVER — Suíte de Documentação Técnica
### Arnês de Testes de Alta Frequência (HFT) e Validação do Protocolo Synapse
*Noxfort Systems — A State Of Art Company*

[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Cobertura](https://img.shields.io/badge/Cobertura-95.7%25-success?style=flat)](../../tests/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-Apache_2.0-blue?style=flat)](../../LICENSE)

---

🌐 **Idiomas:** **[🇺🇸 English](../en/README.md)** • **[🇧🇷 Português (Brasil)](README.md)** • **[🇪🇸 Español](../es/README.md)** • **[🇫🇷 Français](../fr/README.md)** • **[🇷🇺 Русский](../ru/README.md)** • **[🇨🇳 简体中文](../zh/README.md)** • **[📚 Central de Documentação](../README.md)**

---

</div>

## Bem-vindo à Documentação Oficial em Português

Este diretório reúne toda a suíte de documentação técnica em **Português do Brasil** do **CARINA MOCK SERVER** — servidor de teste e validação de telemetria em alta frequência (HFT) e protocolo Synapse do ecossistema de mobilidade autônoma da Noxfort Systems.

Projetado sob rigorosos padrões de **Arquitetura Limpa** e **SOLID**, o Mock Server atua como ambiente de aferição para os agentes neurais de controle de tráfego, simuladores digitais e gateways físicos de campo.

---

## 📚 Índice de Guias Técnicos Especializados

| Documento | Tema & Escopo | Principais Tópicos |
|---|---|---|
| 🏛️ **[Arquitetura do Sistema](architecture.md)** | Especificação Arquitetural | Arquitetura limpa, princípios SOLID, fachada orquestradora (`ReceiverFacade`), concorrência com ThreadPool e isolamento de estado thread-safe. |
| ⚡ **[API do Protocolo Synapse](api_reference.md)** | Especificação gRPC & Protobuf | Serviço `HFTLink`, chamadas `Ping`, `LoadScenario`, `SystemControl` e streaming contínuo de pacotes de tráfego (`StreamTraffic`). |
| 🗺️ **[Mapas e Topologia SUMO](map_and_topology.md)** | Ingestão de Malha Viária | Persistência binária (`LocalMapStorage`), descompactação gzip, extração de geometrias e semáforos (`SumoNetParser`). |
| 🖥️ **[Dashboard Tkinter & Diagnósticos](ui_and_dashboard.md)** | Interface Visual & Telemetria | Painel desktop escuro (`#1e1e2e`), componentes em cartões modulares, medidor de vazão (Hz), motor de detecção de dados zerados e modo headless. |
| 🧪 **[Testes & Garantia de Qualidade](testing.md)** | Validação e Cobertura | Suíte Pytest com 39 testes automatizados, cobertura superior a 95%, mocks determinísticos de contexto gRPC e verificações de concorrência. |
| 🚀 **[Deploy & Conteinerização](deployment.md)** | Docker e Operação em Servidor | Imagem Docker baseada em Python 3.12-slim, `docker-compose.yml`, health checks de socket, variáveis de ambiente e serviço Systemd. |
| 🛠️ **[Guias do Desenvolvedor](developer_guides.md)** | Extensão e Manutenção | Configuração do ambiente local, compilação de arquivos `.proto` com `protoc`, criação de novos cards visuais e padrões de log. |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Engenharia de Mobilidade Inteligente • CARINA MOCK SERVER v1.1.0</i>
</div>
