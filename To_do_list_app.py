#To-Do list Application
# Description: A simple CLI-based to-do manager where users can add, view and delete tasks
#code for to-do list app
tasks = []

while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print()
        n_task = int(input("How many tasks you wants to add :"))
        for i in range(n_task):
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")

    elif choice == "3":
        delete_task = input("enter the task you want to delete :")
        tasks.remove(delete_task)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")



