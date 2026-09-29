# 🛠️ Guias do Desenvolvedor e Manutenção do Código

Este documento reúne instruções práticas para desenvolvedores que desejam modificar, estender ou compilar recursos no **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](../README.md) | 🏛️ [Arquitetura](architecture.md) | ⚡ [Referência da API](api_reference.md) | 🧪 [Testes](testing.md)

---

## 1. Configuração do Ambiente Local

```bash
# Clone do repositório
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER

# Criação e ativação do ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalação das dependências de execução e desenvolvimento
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Compilação do Protobuf Synapse

Caso o arquivo `proto/synapse_hft.proto` seja alterado, execute o compilador do gRPC:

```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

Isso atualizará os módulos Python `synapse_hft_pb2.py` e `synapse_hft_pb2_grpc.py`.

---

## 3. Criação de Novos Cartões para o Dashboard

Todos os componentes visuais herdam da classe abstrata `BaseCard` (`ui/components/base.py`):
1. Crie o novo componente em `ui/components/`.
2. Implemente o método `update_data(self, snapshot: TelemetrySnapshot)`.
3. Instancie o cartão dentro do método `_build_ui` em `ui/dashboard.py`.

---

## 4. Linting e Formatação

O projeto utiliza o **Ruff** para análise estática e formatação de código:
```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guia do Desenvolvedor • CARINA MOCK SERVER</i>
</div>
