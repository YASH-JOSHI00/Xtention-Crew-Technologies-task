import json

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        self.save_tasks()

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                self.save_tasks()
                return f'Task "{task_name}" marked as complete.'
        return f'Task "{task_name}" not found.'

    def display_tasks(self):
        if not self.tasks:
            return "No tasks available."
        output = ""
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            output += f'[{status}] {task.name}: {task.description}\n'
        return output

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            self.tasks = []

def main():
    todo_list = TodoList()
    
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            todo_list.add_task(name, description)
            print(f'Task "{name}" added.')
        elif choice == '2':
            task_name = input("Enter task name to mark as complete: ")
            print(todo_list.mark_task_completed(task_name))
        elif choice == '3':
            print("\nTasks:")
            print(todo_list.display_tasks())
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()





