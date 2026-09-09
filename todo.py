def main():
    my_tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            if not my_tasks:
                print("Your to-do list is empty.")
            else:
                for index, task in enumerate(my_tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "2":
            task = input("Enter a task: ")
            if task.strip():
                my_tasks.append(task)
                print(f"'{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()