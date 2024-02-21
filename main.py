from file_handling import save_tasks_to_file ,load_tasks_from_file
from task_management import *
from interface import menu

print("\nWelcome to the To-Do List Application\n")
menu()
while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(load_tasks_from_file("uncompleted_tasks.json"))
            menu()
        elif choice == '2':
            complete_task(load_tasks_from_file("uncompleted_tasks.json"))
        elif choice == '3':
            view_tasks("uncompleted_tasks.json")
        elif choice == '4':
            delete_task(load_tasks_from_file("uncompleted_tasks.json"))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")