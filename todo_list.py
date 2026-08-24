# To-Do List Project

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\nThank you for using To-Do List!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Start the program
main()
