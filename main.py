from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            task_manager.add_task(task_description)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
