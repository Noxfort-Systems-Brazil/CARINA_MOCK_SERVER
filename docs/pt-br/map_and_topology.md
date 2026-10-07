# 🗺️ Armazenamento de Mapas Viários e Parser de Topologia SUMO

Este documento especifica o subsistema de ingestão, persistência binária e processamento de topologia viária SUMO no **CARINA MOCK SERVER**.

⬅️ [Central de Documentação](README.md) | 🏛️ [Arquitetura](architecture.md) | ⚡ [Referência da API](api_reference.md) | 🖥️ [Interface Tkinter](ui_and_dashboard.md)

---

## 1. Visão Geral e Papel no Ecossistema

No ecossistema CARINA, redes viárias urbanas são modeladas no formato de microssimulação Eclipse SUMO (`.net.xml`). Durante a inicialização de testes, o cliente transmite a topologia completa para o Mock Server através da chamada RPC `LoadScenario`.

O Mock Server processa o ciclo de vida do mapa através de dois componentes de infraestrutura desacoplados:
1. **`LocalMapStorage` (`src/infrastructure/map_storage.py`):** Gerencia a persistência segura dos arquivos binários em disco e a normalização de extensões (`.net.xml`, `.net.xml.gz`).
2. **`SumoNetParser` (`src/infrastructure/sumo_parser.py`):** Realiza o parse do XML viário via biblioteca `sumolib`, extraindo geometrias de faixas e cruzamentos semaforizados (`<tlLogic>`).

---

## 2. Armazenamento Binário em Disco (`LocalMapStorage`)

A classe `LocalMapStorage` implementa a interface `IMapStorage` (`src/core/interfaces.py`):
- **Diretório Padrão:** `data/maps/` (criado automaticamente caso não exista).
- **Normalização de Extensões:** Adiciona `.net.xml` caso o nome não contenha extensão; preserva extensões `.gz` compactadas.
- **Escrita Segura:** Gravação direta de bytes (`bytes map_file_content`) utilizando streams binários do sistema operacional.
- **Localização de Mapas:** Método `get_map_path(map_name)` para reutilização rápida de mapas já gravados.

---

## 3. Parser de Rede SUMO (`SumoNetParser`)

Implementa a interface `IMapParser` e inspeciona o grafo viário:
1. **Faixas e Formas Geométricas:** Itera sobre as arestas (`net.getEdges()`) e faixas (`edge.getLanes()`), extraindo polilinhas (`lane.getShape()`) para renderização vetorial.
2. **Semáforos Físicos:** Itera sobre os nós (`net.getNodes()`), identificando nós do tipo `"traffic_light"`, extraindo coordenadas `(x, y)` e o identificador do semáforo.
3. **Resiliência a Falhas:** Caso `sumolib` não esteja instalado, o parser captura o `ImportError`, emite um aviso no log e retorna coleções vazias sem derrubar o servidor.

---

## 4. Integração com a Interface Visual

As métricas extraídas são enviadas ao `TelemetryState` e apresentadas no **`ScenarioCard`** da interface Tkinter:
- Nome do mapa viário.
- Hash de integridade SHA-256.
- Quantidade total de nós e arestas.
- Tamanho do arquivo recebido em kilobytes.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guia de Armazenamento e Topologia • CARINA MOCK SERVER</i>
</div>
