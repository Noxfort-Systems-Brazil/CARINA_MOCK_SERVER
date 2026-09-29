# 🖥️ Panel Gráfico Tkinter y Diagnóstico en Tiempo Real

Este documento detalla la interfaz gráfica de usuario, los componentes modulares y el motor de diagnóstico de **CARINA MOCK SERVER**.

⬅️ [Centro de Documentación](../README.md) | 🏛️ [Arquitectura](architecture.md) | ⚡ [Referencia de la API](api_reference.md) | 🧪 [Pruebas](testing.md)

---

## 1. Arquitectura de la Interfaz Visual

El panel está desarrollado en **Tkinter** nativo de Python, estructurado en tarjetas modulares desacopladas con paleta visual oscura (`ui/theme.py`).

### 1.1 Ciclo de Consulta No Bloqueante
La interfaz consulta el estado del servidor cada **250 milisegundos** (`self.root.after(250, self._update_loop)`):
- Obtiene un `TelemetrySnapshot` inmutable de `TelemetryState`.
- Ejecución fluida sin bloqueos en la interfaz ni interferencia en el streaming gRPC.

---

## 2. Componentes de la Interfaz

1. **Encabezado (`ui/components/header.py`):** Logotipo y distintivo de estado de conexión activa/inactiva.
2. **Tarjeta de Conexión (`ui/components/connection_card.py`):** Dirección gRPC, estado del sistema (`IDLE`, `RUNNING`) y tiempo desde el último latido.
3. **Tarjeta de Escenario (`ui/components/scenario_card.py`):** Nombre del mapa, hash de integridad, recuento de nodos/aristas y tamaño.
4. **Tarjeta de Flujo (`ui/components/stream_card.py`):** Contador de tramas, ID de secuencia y frecuencia calculada en Hertz.
5. **Tarjeta de Diagnóstico (`ui/components/diagnostics_card.py`):** Alerta visual de datos activos o en cero (🟢 DADOS ATIVOS vs ⚠️ DADOS ZERADOS), carriles activos y tabla de muestreo.
6. **Tarjeta de Eventos (`ui/components/events_card.py`):** Historial en tiempo real de los últimos 15 eventos del servidor.

---

## 3. Modo Headless (Sin Interfaz Gráfica)

Para entornos en la nube, contenedores Docker y flujos de CI/CD:
```bash
python main.py --no-gui
# O mediante variable de entorno:
MOCK_SERVER_NO_GUI=1 python main.py
```
Si Tkinter no puede abrir una pantalla por falta de servidor gráfico, el sistema conmuta automáticamente al modo headless.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Guía de Interfaz y Diagnóstico • CARINA MOCK SERVER</i>
</div>
