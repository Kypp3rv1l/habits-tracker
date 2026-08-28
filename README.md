# Habit Tracker CLI

Pequeña aplicación de línea de comandos para llevar el registro de hábitos diarios.
Proyecto creado como evidencia de la Actividad N°1: Control de Versiones (Trabajo en equipo).

## ¿Qué hace?

- Agrega hábitos a seguir.
- Marca un hábito como completado en el día de hoy.
- Lista los hábitos y cuántos días se han completado.
- Muestra estadísticas por hábito.

Los datos se guardan localmente en `habits.json`.

## Cómo clonar el proyecto

```bash
git clone https://github.com/<tu-usuario>/habit-tracker.git
cd habit-tracker
```

## Cómo ejecutarlo

Requiere Python 3.

```bash
python app.py
```

Desde una sesión interactiva de Python puedes usar las funciones directamente:

```python
from app import add_habit, mark_done, list_habits, show_stats

add_habit("Leer 20 minutos")
mark_done("Leer 20 minutos")
list_habits()
show_stats("Leer 20 minutos")
```

## Cómo contribuir

1. Crea una rama a partir de `main`: `git checkout -b feature/nombre-de-tu-cambio`.
2. Realiza commits pequeños y con mensajes claros y descriptivos.
3. Antes de subir tus cambios, sincroniza con `main` (usa `rebase` para mantener el historial limpio).
4. Abre un Pull Request describiendo el cambio.

## Historial de versiones

- `v1.0`: primera versión funcional (agregar, listar, marcar completado y estadísticas).
- `v1.1`: limpieza de historial de commits y documentación final.

## Evidencia de control de versiones

Este repositorio incluye, como parte de la actividad:
- Commit inicial y commits regulares y significativos.
- Una rama de desarrollo (`feature/stats`) fusionada a `main`.
- Un conflicto de merge simulado y resuelto (rama `conflict-demo`).
- Uso de `git stash` para guardar cambios temporales.
- Un `rebase` interactivo para limpiar el historial de commits.
- Tags (`v1.0` y `v1.1`) marcando versiones del proyecto.
