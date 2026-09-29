# 🧪 Pruebas Automatizadas y Control de Calidad

Este documento define la estrategia de pruebas, requisitos de cobertura y procedimientos de validación de **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](../README.md) | 🏛️ [Arquitectura](architecture.md) | ⚡ [Referencia de la API](api_reference.md) | 🚀 [Despliegue](deployment.md)

---

## 1. Estándares de Calidad y Cobertura

- **Motor de Pruebas:** `pytest` con `pytest-cov`.
- **Cobertura Mínima Obligatoria:** **80%** (configurada en `pyproject.toml`).
- **Cobertura Actual:** **95.7%** en todos los módulos bajo `src/`.
- **Total de Pruebas:** 39 casos unitarios e integrados que se ejecutan en menos de 1 segundo.

---

## 2. Módulos de Prueba (`tests/`)

- `test_config.py`: Parámetros predeterminados y variables de entorno.
- `test_grpc_server.py`: Ciclo de vida del servidor gRPC y pruebas de ping.
- `test_hft_service.py`: Manejo de RPCs, carga de mapas, streaming y control de errores.
- `test_loggers.py`: Registros en consola, archivo rotativo y compuesto.
- `test_map_storage.py`: Almacenamiento binario de mapas y extensiones automáticas.
- `test_receiver_facade.py`: Orquestador principal y conmutación a modo headless.
- `test_sumo_parser.py`: Análisis de XML de SUMO y tolerancia a archivos inválidos.
- `test_telemetry_state.py`: Concurrencia multihilo, tasa en Hz, detección de ceros y tiempos de espera.

---

## 3. Comandos de Ejecución

```bash
# Ejecución completa con cobertura
pytest

# Ejecución de un módulo específico
pytest tests/test_hft_service.py -v

# Generación de reporte HTML
pytest --cov=src --cov-report=html
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Control de Calidad y Pruebas • CARINA MOCK SERVER</i>
</div>
