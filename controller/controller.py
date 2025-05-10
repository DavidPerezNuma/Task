from model.task import Task 

class Controller:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        self.tasks.append(Task(title, description))

    def edit_task(self, index, new_title, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
            self.tasks[index].description = new_description

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def get_tasks(self):
        return self.tasks
