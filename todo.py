# ── TO-DO LIST APP ──────────────────────────

tasks = []   # list to store all tasks

# ── FUNCTIONS ───────────────────────────────

def add_task(name):
    tasks.append({"name": name, "done": False})
    print("✓ Task added:", name)

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet! Add one first.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"  {i+1}. [{status}] {task['name']}")

def mark_done(number):
    index = number - 1
    if index < 0 or index >= len(tasks):
        print("Invalid number! Try again.")
        return
    tasks[index]["done"] = True
    print("✓ Marked done:", tasks[index]["name"])

def delete_task(number):
    index = number - 1
    if index < 0 or index >= len(tasks):
        print("Invalid number! Try again.")
        return
    removed = tasks.pop(index)
    print("🗑 Deleted:", removed["name"])

# ── MAIN MENU LOOP ───────────────────────────

print("Welcome to your To-Do List!")

while True:
    print("\n--- MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task done")
    print("4. Delete task")
    print("5. Quit")

    choice = input("\nChoose (1-5): ")

    if choice == "1":
        name = input("Enter task name: ")
        add_task(name)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        try:
            num = int(input("Task number to mark done: "))
            mark_done(num)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        view_tasks()
        try:
            num = int(input("Task number to delete: "))
            delete_task(num)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        print("Goodbye! Stay productive!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")