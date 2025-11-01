import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a number.\n")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = f"[Done] {tasks[num - 1]}"
            save_tasks(tasks)
            print("✅ Task marked as complete!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("===== 🧩 To-Do List =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task complete")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()
