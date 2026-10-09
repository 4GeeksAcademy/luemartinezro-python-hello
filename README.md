# Todo List CLI

A lightweight command-line task manager built for the internal tools team at a logistics company. Operations coordinators can quickly manage daily tasks directly from the terminal without losing progress between shifts.

## Features

- **Add a task** — Register new tasks as they come in
- **List tasks** — View all pending tasks with clear numeric positions
- **Delete a task** — Remove a completed task by selecting its list position
- **Persist data** — Tasks are automatically saved to `todos.csv` and reloaded when you restart the app
- **No external dependencies** — Uses only the Python standard library (`csv`, `os`)

## How to use

Run the application from your terminal:

```bash
$ python main.py
```

Once started, you'll see an interactive menu:

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

### Commands

| Option | Action |
|---|---|
| `a` | Add a new task (you'll be prompted for the title) |
| `l` | List all pending tasks with their numbers |
| `d` | Delete a task by entering its list number |
| `q` | Quit the application |

Your tasks are automatically saved to `todos.csv` whenever you add or delete an item, and are loaded back the next time you run the program.

## Requirements

- Python 3.6+ (the `csv` module is part of the standard library)

## Project structure

```
.
├── main.py       # The Todo List CLI application
├── server.py     # Flask server (legacy, not required for this tool)
├── README.md     # This file
└── todos.csv     # Auto-generated task storage (created on first use)
```

## License

This project was built as part of the [4Geeks Python Resources](https://4geeks.com/technology/python) for learning at [4Geeks.com](https://4geeks.com).
