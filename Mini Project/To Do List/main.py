
tasks = [ 
    "Solve maths problems",
    "Write a poem",
    "Create a short story",
]

def add_task():
    task = input("Enter task to add : ")
    tasks.append(task)
    print(" Task added successfully! \n ")

def remove_task():
    if len(tasks) == 0:
        print(" No tasks available to remove.")
        return

    print("Your Tasks")
    for index, task in enumerate(tasks, start=1):
        print(index, task)

    pop_task = int(input("Enter task number to remove : "))

    if pop_task <= len(tasks) :
        index = pop_task - 1
        tasks.pop(index)

    print(" Task Removed Successfully! \n")

def view_task():
    if len(tasks) == 0:
        print(" No tasks available.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(index , task)

def Exit():
    print(" Exiting To Do List \n")
    

while True:

    print("\n 1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

    choice = int(input("Enter choice : "))
    if choice == 1 :
        add_task()
    elif choice == 2 :
        remove_task()
    elif choice == 3 :
        view_task()
    elif choice == 4 :
        Exit()
        break
    else:
        print(" Invalid Choice!! ")




