# Build a TO-Do List Application while you are fixing your room
# I suggest that you build one using tkinter after this 
class Todo:
    def __init__(self):
        # Create an empty list to store the tasks
        self.tasks = []
        
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number!")
            return 
        self.tasks.pop(index-1)
        
    def display_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
            return 
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
            
    def run(self):
        while True:
            print("\nTo-Do App")
            print("1. Add a Task")
            print("2. Remove a Task")
            print("3. Display ALL Tasks")
            print("4. Exit")
            
            choice = input("Enter you choice: ")
            
            if choice == "1":
                task = input("Enter the task description: ")
                self.add_task(task)
                print("Task added successfully!")
            elif choice == "2":
                self.display_tasks()
                task_num = int(input("Enter the task number to remove: "))
                self.remove_task(task_num)
                print("Task removed successfully!")
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")
                
if __name__ == "__main__":
    todo_app = Todo()
    todo_app.run()
'''
class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number!")
            return
        self.tasks.pop(index - 1)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def run(self):
        while True:
            print("\nTo-Do App")
            print("1. Add a Task")
            print("2. Remove a Task")
            print("3. Display All Tasks")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task description: ")
                self.add_task(task)
                print("Task added successfully!")
            elif choice == "2":
                self.display_tasks()
                task_num = int(input("Enter the task number to remove: "))
                self.remove_task(task_num)
                print("Task removed successfully!")
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    todo_app = ToDo()
    todo_app.run()
    
'''