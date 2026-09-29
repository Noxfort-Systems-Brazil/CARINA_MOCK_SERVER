# 🧪 Diretrizes de Testes e Garantia de Qualidade

Este documento detalha a suíte de testes automatizados, cobertura de código e procedimentos de validação do **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](../README.md) | 🏛️ [Arquitetura](architecture.md) | ⚡ [Referência da API](api_reference.md) | 🚀 [Deploy](deployment.md)

---

## 1. Padrões de Qualidade e Cobertura

O CARINA MOCK SERVER adota rigorosos requisitos de qualidade para assegurar confiabilidade no tráfego de dados críticos de controle semafórico:
- **Ferramenta de Execução:** `pytest` com plugin `pytest-cov`.
- **Limite Mínimo de Cobertura:** **80%** (exigido via `--cov-fail-under=80`).
- **Cobertura Atingida:** **95,7%** no código fonte sob `src/`.
- **Total de Testes:** 39 casos de teste unitários e de integração executados em menos de 1 segundo.

---

## 2. Estrutura dos Módulos de Teste (`tests/`)

- `test_config.py`: Validação das portas e endereços padrões e sobreposição por variáveis de ambiente.
- `test_grpc_server.py`: Ciclo de vida do servidor de rede, ligação de portas e chamadas gRPC de ping.
- `test_hft_service.py`: Tratamento de RPCs de ping, carga de cenário com salvamento de mapa, comandos operacionais e streaming com cancelamento e erros.
- `test_loggers.py`: Comportamento dos loggers de console, arquivo rotativo e registrador composto.
- `test_map_storage.py`: Armazenamento de arquivos binários de malha viária, extensões automáticas e resiliência a falhas de gravação.
- `test_receiver_facade.py`: Configuração do orquestrador principal, modo headless e fallback automático em ambientes sem interface.
- `test_sumo_parser.py`: Leitura de XMLs do simulador SUMO, extração de vias e tratamento de arquivos inexistentes ou corrompidos.
- `test_telemetry_state.py`: Testes de concorrência multithread com travas, cálculo de vazão em Hz, detecção de pacotes zerados e timeout de inatividade.

---

## 3. Comandos de Execução

```bash
# Execução padrão dos testes com relatório de cobertura no terminal
pytest

# Execução direcionada a um módulo específico
pytest tests/test_hft_service.py -v

# Geração de relatório visual detalhado em HTML
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Garantia de Qualidade e Testes • CARINA MOCK SERVER</i>
</div>
