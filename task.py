# In task.py
class Task:
    def __init__(self, description, due_date=None, completed=False, priority='low', tags=None, id=None):
        self.description = description
        self.due_date = due_date
        self.status = completed
        self.priority = priority
        self.tags = tags if tags else []
        self.id = id

    def __str__(self):
        status = "Completed" if self.status else "Pending"
        return f"{self.id}. - {self.description} - Due Date: {self.due_date} - Priority: {self.priority} - Tags: {', '.join(self.tags)} - {status}"
