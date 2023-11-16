class ToDoList():
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        return self.task_list.append(task)
    
    def completed_task(self, task):
        if task not in self.task_list:
            raise Exception("Task is not on task-tracker")
        return self.task_list.remove(task)