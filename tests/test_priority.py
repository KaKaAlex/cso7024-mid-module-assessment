import pytest

from taskmanager import core


def test_add_task_with_priority():
    tasks = core.add_task([], "Write report", "high")
    assert tasks[0]["priority"] == "high"


def test_add_task_default_priority_is_medium():
    tasks = core.add_task([], "Write report")
    assert tasks[0]["priority"] == "medium"


def test_tasks_with_priority_filters_matching_tasks():
    tasks = []
    tasks = core.add_task(tasks, "Urgent task", "high")
    tasks = core.add_task(tasks, "Normal task", "medium")
    tasks = core.add_task(tasks, "Another urgent task", "high")

    high_tasks = core.tasks_with_priority(tasks, "high")

    assert len(high_tasks) == 2
    assert high_tasks[0]["title"] == "Urgent task"
    assert high_tasks[1]["title"] == "Another urgent task"


def test_add_task_invalid_priority_raises_value_error():
    with pytest.raises(ValueError):
        core.add_task([], "Wrong priority", "urgent")