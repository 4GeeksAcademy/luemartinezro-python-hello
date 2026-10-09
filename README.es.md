# Todo List CLI

Un administrador de tareas ligero desde la línea de comandos, creado para el equipo de herramientas internas de una empresa de logística. Los coordinadores de operaciones pueden gestionar sus tareas diarias directamente desde el terminal sin perder el progreso entre turnos.

## Funcionalidades

- **Agregar tarea** — Registra nuevas tareas a medida que aparecen
- **Listar tareas** — Muestra todas las tareas pendientes con posiciones numéricas claras
- **Eliminar tarea** — Elimina una tarea completada seleccionando su posición en la lista
- **Persistencia de datos** — Las tareas se guardan automáticamente en `todos.csv` y se recargan al reiniciar la aplicación
- **Sin dependencias externas** — Utiliza solo la biblioteca estándar de Python (`csv`, `os`)

## Cómo usar

Ejecuta la aplicación desde tu terminal:

```bash
$ python main.py
```

Al iniciar, verás un menú interactivo:

```
==============================
   TODO LIST MANAGER
==============================
  [a] Add a task
  [l] List all tasks
  [d] Delete a task
  [q] Quit
==============================
```

### Comandos

| Opción | Acción |
|---|---|
| `a` | Agregar una nueva tarea (se te pedirá el título) |
| `l` | Listar todas las tareas pendientes con sus números |
| `d` | Eliminar una tarea ingresando su número en la lista |
| `q` | Salir de la aplicación |

Las tareas se guardan automáticamente en `todos.csv` cada vez que agregas o eliminas un elemento, y se cargan nuevamente la próxima vez que ejecutes el programa.

## Requisitos

- Python 3.6+ (el módulo `csv` es parte de la biblioteca estándar)

## Estructura del proyecto

```
.
├── main.py       # La aplicación Todo List CLI
├── server.py     # Servidor Flask (legado, no requerido para esta herramienta)
├── README.es.md  # Este archivo
└── todos.csv     # Almacenamiento de tareas (se crea automáticamente en el primer uso)
```

## Licencia

Este proyecto fue creado como parte de los [Recursos de Python de 4Geeks](https://4geeks.com/es/technology/python) para el aprendizaje en [4Geeks.com](https://4geeks.com).
