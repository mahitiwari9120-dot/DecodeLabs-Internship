# ==========================================
# Python Project 1 - To-Do List
# DecodeLabs Industrial Training
# ==========================================

tasks = []


def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        print("\nTask added successfully!")
    else:
        print("\nTask cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    while True:
        print("\n==============================")
        print("        TO-DO LIST")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

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
