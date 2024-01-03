class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "status": "Pending"})

    def list_tasks(self):
        return [task["name"] for task in self.tasks]

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["name"] == task:
                t["status"] = "Completed"

    def clear_tasks(self):
        self.tasks = []

# Main program logic
if __name__ == "__main__":
    todo_manager = ToDoListManager()


