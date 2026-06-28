"""Core task operations for the CSO7024 task manager.

Tasks are represented as plain dictionaries so the data is easy to inspect
and to serialise to JSON. A task currently has three fields:

    id     an integer, unique within the list
    title  a non-empty string
    done   a boolean, False when the task is created

Every operation returns a *new* list rather than modifying its argument. This
keeps the functions easy to test and reason about.

In the mid-module assessment you will extend this module with a task
"priority" and the ability to filter by it. The exact specification is in the
README. Do not change the behaviour the existing tests rely on.
"""

from __future__ import annotations

import json
from pathlib import Path


def add_task(
    tasks: list[dict],
    title: str,
    priority: str = "medium"
) -> list[dict]:
    """Return a new task list with one task appended."""
    if title is None or not title.strip():
        raise ValueError("Task title must not be empty")

    allowed_priorities = ["high", "medium", "low"]

    if priority not in allowed_priorities:
        raise ValueError("Priority must be high, medium or low")

    next_id = max((task["id"] for task in tasks), default=0) + 1

    new_task = {
        "id": next_id,
        "title": title.strip(),
        "done": False,
        "priority": priority,
    }

    return tasks + [new_task]

def tasks_with_priority(tasks: list[dict], priority: str) -> list[dict]:
    """Return tasks that match the given priority."""
    return [task for task in tasks if task["priority"] == priority]


def complete_task(tasks: list[dict], task_id: int) -> list[dict]:
    """Return a new task list with the task of ``task_id`` marked done.

    Raises:
        KeyError: if no task has the given id.
    """
    if not any(task["id"] == task_id for task in tasks):
        raise KeyError(f"No task with id {task_id}")
    return [
        {**task, "done": True} if task["id"] == task_id else task
        for task in tasks
    ]


def remove_task(tasks: list[dict], task_id: int) -> list[dict]:
    """Return a new task list with the task of ``task_id`` removed.

    Raises:
        KeyError: if no task has the given id.
    """
    if not any(task["id"] == task_id for task in tasks):
        raise KeyError(f"No task with id {task_id}")
    return [task for task in tasks if task["id"] != task_id]


def load_tasks(path: Path) -> list[dict]:
    """Load tasks from a JSON file, returning an empty list if it is absent."""
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_tasks(tasks: list[dict], path: Path) -> None:
    """Write tasks to a JSON file as indented JSON."""
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
