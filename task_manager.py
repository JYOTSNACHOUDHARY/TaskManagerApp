from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    # In task_manager.py


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def get_tasks(self):
        return self.tasks



    def add_task(
        self, description, due_date=None, priority="low", tags=None, completed="Pending"
    ):
        task = Task(
            description,
            due_date=due_date,
            priority=priority,
            tags=tags,
            completed=completed,
            id=self.next_id,
        )
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def edit_task(self, task_id, new_description, due_date= None, completed = None, priority=None):
        if 1 <= task_id <= len(self.tasks):
            index = task_id - 1
            self.tasks[index].description = new_description
            self.tasks[index].due_date = due_date
            self.tasks[index].status = completed
            self.tasks[index].priority = priority

            print("Task description updated successfully.")
        else:
            print("Invalid task index.")

    def mark_task_incomplete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = False
            print("Task marked as incomplete.")
        else:
            print("Invalid task index.")

    def search_by_keyword(self, keyword):
        result = [
            task for task in self.tasks if keyword.lower() in task.description.lower()
        ]
        if result:
            print("Matching tasks:")
            for task in result:
                print(task)
        else:
            print("No matching tasks found.")

    def filter_by_priority(self, priority):
        result = [
            task for task in self.tasks if task.priority.lower() == priority.lower()
        ]
        if result:
            print(f"Tasks with priority '{priority}':")
            for task in result:
                print(task)
        else:
            print(f"No tasks with priority '{priority}' found.")
