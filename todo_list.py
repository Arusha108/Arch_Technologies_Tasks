import json
import os

tasks_file = "tasks.json"

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    title = input("Enter task description: ").strip()
    category = input("Enter category (e.g., Work, Personal): ").strip()
    tasks.append({"title": title, "category": category, "completed": False})
    print("Task added.")

def view_tasks(tasks, show_completed=False, filter_category=None):
    filtered = [t for t in tasks if t["completed"] == show_completed]
    if filter_category:
        filtered = [t for t in filtered if t["category"].lower() == filter_category.lower()]
    if not filtered:
        print("No tasks to show.")
        return
    for idx, t in enumerate(filtered, 1):
        print(f"{idx}. {t['title']} [{t['category']}]" + (" (Completed)" if t["completed"] else ""))

def mark_completed(tasks):
    view_tasks(tasks, show_completed=False)
    idx = input("Enter the number of the task to mark as completed: ").strip()
    if idx.isdigit():
        idx = int(idx) - 1
        incomplete = [i for i, t in enumerate(tasks) if not t["completed"]]
        if 0 <= idx < len(incomplete):
            tasks[incomplete[idx]]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid selection.")
    else:
        print("Invalid input.")

def remove_task(tasks):
    view_tasks(tasks, show_completed=False)
    idx = input("Enter the number of the task to remove: ").strip()
    if idx.isdigit():
        idx = int(idx) - 1
        incomplete = [i for i, t in enumerate(tasks) if not t["completed"]]
        if 0 <= idx < len(incomplete):
            del tasks[incomplete[idx]]
            print("Task removed.")
        else:
            print("Invalid selection.")
    else:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. View Completed Tasks")
        print("4. Mark Task as Completed")
        print("5. Remove Task")
        print("6. Filter Tasks by Category")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks, show_completed=False)
        elif choice == "3":
            view_tasks(tasks, show_completed=True)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            remove_task(tasks)
        elif choice == "6":
            cat = input("Enter category to filter: ").strip()
            view_tasks(tasks, show_completed=False, filter_category=cat)
        elif choice == "7":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        save_tasks(tasks)

if __name__ == "__main__":
    main()
