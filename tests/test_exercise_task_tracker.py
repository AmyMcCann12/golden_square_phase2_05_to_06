import pytest #type: ignore
from lib.exercise_task_tracker import *

"""
If no tasks have been added, return an empty list of tasks
"""
def test_task_tracker_no_tasks_added():
    to_do_list = ToDoList()
    assert to_do_list.task_list == []

"""
If one task has been added, 
shows that one task in the task_list 
"""
def test_task_tracker_one_task_added():
    to_do_list = ToDoList()
    to_do_list.add_task("Walk the dog")
    assert to_do_list.task_list == ["Walk the dog"]

"""
If three tasks are added, 
shows all three tasks in the task_list 
"""
def test_task_tracker_three_tasks_added():
    to_do_list = ToDoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Do the food shop")
    to_do_list.add_task("Make tea")
    assert to_do_list.task_list == ["Walk the dog", "Do the food shop", "Make tea"]

""" If a task is inputted as complete but is not in the task_list, raise an error
"""
def test_tracker_completed_task_not_on_task_list():
    to_do_list = ToDoList()
    with pytest.raises(Exception) as err:
        to_do_list.completed_task("Walk the dog")
    assert str(err.value) == "Task is not on task-tracker"

"""
If one task has been added, and then completed, 
shows an empty task list that one task in the task_list 
"""
def test_task_tracker_one_task_added_then_completed():
    to_do_list = ToDoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.completed_task("Walk the dog")
    assert to_do_list.task_list == []

"""
If three tasks have been added, and then one is completed, 
shows the remaining two tasks in the task list
"""
def test_task_tracker_three_added_one_completed():
    to_do_list = ToDoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Do the food shop")
    to_do_list.completed_task("Walk the dog")
    to_do_list.add_task("Make tea")
    assert to_do_list.task_list == ["Do the food shop", "Make tea"]