# Empty list to store tasks
tasks = []

while True:
    print("\nTO-DO LIST:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Clear all tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        new_task = input("Enter the task to add: ")
        tasks.append(new_task)
        print("Task added:", new_task)

    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_index <= len(tasks):
                print(f"Completed task: {tasks.pop(task_index - 1)}")
            else:
                print("Invalid task number.")

    elif choice == '4':
        tasks.clear()
        print("All tasks cleared.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
