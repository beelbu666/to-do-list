import json


def show_options():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task(task):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append({"ID": len(tasks) + 1, "Task": task, "Status": False})

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

    print("Task added successfully.")


def view_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Done" if task["Status"] else "Not Done"
        print(f"ID: {task['ID']}, Task: {task['Task']}, Status: {status}")


def mark_task_done(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks available to mark as done.")
        return
    
    for task in tasks:
        if task["ID"] == task_id:
            task["Status"] = True
            print(f"Task {task_id} marked as done.")
            break
    else:
        print("Task ID not found.")
        return

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def delete_task(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        if task["ID"] == task_id:
            del tasks[i]
            print(f"Task {task_id} deleted successfully.")
            break
    else:
        print("Task ID not found.")
        return
    
    # Update IDs after deletion
    for i, task in enumerate(tasks):
        task["ID"] = i + 1
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def press_any_key_to_continue():
    print("\n")
    input("Press Enter to continue...")
    print("\n")

def main():
    Status = True
    while True:
        show_options()
        choice = input("Enter your choice (1-5): ")
        print("\n")

        if choice == "1":
            view_tasks()
            task = input("Enter the task: ")
            print("\n")
            add_task(task)
            press_any_key_to_continue()

        elif choice == "2":
            view_tasks()
            press_any_key_to_continue()

        elif choice == "3":
            view_tasks()
            task_id = int(input("Enter task ID to mark as done: "))
            print("\n")
            mark_task_done(task_id)
            press_any_key_to_continue()

        elif choice == "4":
            view_tasks()
            task_id = int(input("Enter task ID to delete: "))
            print("\n")
            delete_task(task_id)
            press_any_key_to_continue()

        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
