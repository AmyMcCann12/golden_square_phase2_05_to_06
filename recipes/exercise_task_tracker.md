## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDoList:
    # There will be no User-facing properties:

    def __init__(self):
        # Public Property:
        #   task_list: empty list
        # Side effects:
        #   Sets the task_list property equal to an empty list
        pass # No code here yet

  def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   updated task_list
        # Side-effects
        #   Saves the task to the self.task_list object
        pass # No code here yet

    def completed_task(self, task):
        # Paramters:
        #   task: string representing a single task that has been completed
        # Returns:
        #   updated task_list
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# EXAMPLE

"""
If no tasks have been added, return an empty list of tasks
"""
to_do_list = ToDoList()
to_do_list.task_list # => []

"""
If one task has been added, shows that one task in the task_list 
"""
to_do_list = ToDoList()
to_do_list.add_task("Walk the dog")
to_do_list.task_list # => ["Walk the dog"]

"""
If three tasks are added, shows all three tasks in the task_list 
"""
to_do_list = ToDoList()
to_do_list.add_task("Walk the dog")
to_do_list.add_task("Do the food shop")
to_do_list.add_task("Make tea")
to_do_list.task_list # => ["Walk the dog", "Do the food shop", "Make tea"]

""" If a task is inputted as complete but is not in the task_list, raise an error
"""
to_do_list = ToDoList()
to_do_list.completed_task("Walk the dog")
to_do_list.task_list # => "Task is not on task-tracker"

"""
If one task has been added, and then completed, shows an empty task list that one task in the task_list 
"""
to_do_list = ToDoList()
to_do_list.add_task("Walk the dog")
to_do_list.completed_task("Walk the dog")
to_do_list.task_list # => []

"""
If three tasks have been added, and then one is completed, shows the remaining two tasks in the task list
"""
to_do_list = ToDoList()
to_do_list.add_task("Walk the dog")
to_do_list.add_task("Do the food shop")
to_do_list.completed_task("Walk the dog")
to_do_list.add_task("Make tea")
to_do_list.task_list # => ["Walk the dog", "Make tea"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._