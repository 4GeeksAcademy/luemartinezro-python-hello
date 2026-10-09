"""Todo List CLI — A lightweight command-line task manager.

Operations coordinators can add, view, and delete tasks.
Tasks are persisted to a local CSV file so they survive terminal restarts.
Uses only the Python standard library.
"""

import csv
import os

# ---------------------------------------------------------------------------
# In-memory storage
# ---------------------------------------------------------------------------
TASKS: list[str] = []
CSV_FILE = "todos.csv"


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------
def add_one_task(title: str) -> None:
    """Append a new task to the in-memory list."""
    TASKS.append(title)


def print_list() -> None:
    """Display all pending tasks with their 1-based numeric position."""
    if not TASKS:
        print("🎯 No pending tasks. Enjoy your day!")
        return
    print("\n📋 Your To-Do List:")
    print("-" * 30)
    for i, task in enumerate(TASKS, start=1):
        print(f"  {i}. {task}")
    print("-" * 30)


def delete_task(number_to_delete: int) -> None:
    """Remove one task by its 1-based list position.

    Args:
        number_to_delete: 1-based position of the task to remove.
    """
    if 1 <= number_to_delete <= len(TASKS):
        removed = TASKS.pop(number_to_delete - 1)
        print(f"🗑️  Deleted: {removed}")
    else:
        print(f"❌ Invalid task number. Please choose between 1 and {len(TASKS)}.")


def save_todos() -> None:
    """Persist the current task list into a CSV file."""
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title"])
        for task in TASKS:
            writer.writerow([task])


def load_todos() -> None:
    """Load tasks from the CSV file back into memory.

    Calling this replaces the current in-memory list with the file contents.
    If the file does not exist, the list is left empty.
    """
    global TASKS
    if not os.path.exists(CSV_FILE):
        TASKS = []
        return

    loaded: list[str] = []
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            loaded.append(row["title"])
    TASKS = loaded


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main() -> None:
    """Run the interactive Todo List CLI."""
    load_todos()

    while True:
        print("\n" + "=" * 30)
        print("   TODO LIST MANAGER")
        print("=" * 30)
        print("  [a] Add a task")
        print("  [l] List all tasks")
        print("  [d] Delete a task")
        print("  [q] Quit")
        print("=" * 30)

        choice = input("Your choice: ").strip().lower()

        if choice == "a":
            title = input("Task title: ").strip()
            if title:
                add_one_task(title)
                save_todos()
                print(f"✅ Added: {title}")
            else:
                print("⚠️  Task title cannot be empty.")
        elif choice == "l":
            print_list()
        elif choice == "d":
            print_list()
            if TASKS:
                try:
                    num = int(input("Number of the task to delete: ").strip())
                    delete_task(num)
                    save_todos()
                except ValueError:
                    print("❌ Please enter a valid number.")
        elif choice == "q":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Choose a, l, d, or q.")


if __name__ == "__main__":
    main()