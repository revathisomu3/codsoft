# Initialize an empty list to store tasks
tasks = []

# Function to add a new task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to mark a task as completed
def complete_task(task_idx):
    if 1 <= task_idx <= len(tasks):
        completed_task = tasks.pop(task_idx - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_task = input("Enter the task description: ")
        add_task(new_task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        print("Thank you for using the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
    