# 🛠️ Guide du Développeur & Contribution

Ce document rassemble les directives de développement, de compilation et d'extension pour **CARINA MOCK SERVER**.

⬅️ [Centre de Documentation](../README.md) | 🏛️ [Architecture](architecture.md) | ⚡ [Référence API](api_reference.md) | 🧪 [Tests](testing.md)

---

## 1. Environnement de Développement Local

```bash
git clone https://github.com/Noxfort-Systems-Brazil/CARINA_MOCK_SERVER.git
cd CARINA_MOCK_SERVER
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 2. Compilation Protobuf

Pour régénérer les fichiers gRPC après modification de `proto/synapse_hft.proto` :
```bash
python -m grpc_tools.protoc \
  -Iproto \
  --python_out=proto \
  --grpc_python_out=proto \
  proto/synapse_hft.proto
```

---

## 3. Ajout de Cartes Graphiques sur le Tableau de Bord

Toutes les cartes héritent de la classe de base `BaseCard` (`ui/components/base.py`) :
1. Définissez la nouvelle carte dans `ui/components/`.
2. Implémentez la méthode `update_data(self, snapshot: TelemetrySnapshot)`.
3. Instanciez le composant dans la méthode `_build_ui()` de `ui/dashboard.py`.

---

## 4. Analyse et Formatage avec Ruff

```bash
ruff check .
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guide du Développeur • CARINA MOCK SERVER</i>
</div>
