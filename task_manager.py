from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index-1]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
