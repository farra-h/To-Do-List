from datetime import datetime
from file_handling import save_tasks_to_file ,load_tasks_from_file
# add task
def add_task(tasks):
    task_name = input("Enter new task: ")
    details = input("Enter task details: ")
    remaining_time = due_date()
    priority = int(input("Enter task priority (1 to 3): "))
    while priority not in [1, 2, 3]:
        print("Invalid priority. Please enter a number between 1 and 3.")
        priority = int(input("Enter task priority (1 to 3): "))
    tasks[task_name] = {"details": details, "priority": priority ,"deadline": remaining_time[0]}
    save_tasks_to_file(tasks, "uncompleted_tasks.json")
    print(f" \n{task_name} has been added to the list.\n")

###########################################################################################################
# delete task
def delete_task(tasks):
    view_tasks("uncompleted_tasks.json")
    while True:
        try:
            number = int(input("enter the number of task you want to remove:"))
            tasks = load_tasks_from_file("uncompleted_tasks.json")
            tasks = list(tasks.items())

            if tasks[number - 1] != " ":
                tasks.pop(number - 1)
                print("delete")
                dictionary = dict(tasks)

                save_tasks_to_file(dictionary, "uncompleted_tasks.json")
                view_tasks("uncompleted_tasks.json")
            break

        except():
            print("invalid input")
#####################################################################################################
# view task
def view_tasks(filename):
    tasks = load_tasks_from_file(filename)
    if not tasks:
        print("No tasks found.")
    else:
        sorted_tasks = sorted(tasks.items(), key=lambda x:int( x[1]['priority']))
        for i, (task, details) in enumerate(sorted_tasks, start=1):
            print(f"Task number: {i}\nTask name: {task}\nDetails: {details['details']}\nPriority: {details['priority']}\nDeadline: {details['deadline']} day")
            print("-" * 50)

###############################################################################################################################
# move to completed
def move_to_completed(task_to_move):
    completed_tasks = load_tasks_from_file("completed_tasks.json")
    completed_tasks.update(task_to_move)
    save_tasks_to_file(completed_tasks, "completed_tasks.json")

#######################################################################################################################
# complete task 

def complete_task(tasks):
    view_tasks("uncompleted_tasks.json")
    while True:
        try:
            task_index = int(input("Enter the number of the task you want to mark as completed: "))
            if 0 < task_index <= len(tasks):
                task_to_complete = list(tasks.keys())[task_index - 1]
                move_to_completed({task_to_complete: tasks[task_to_complete]})
                del tasks[task_to_complete]
                save_tasks_to_file(tasks, "uncompleted_tasks.json")
                print(f"Task '{task_to_complete}' has been marked as completed.")
            else:
                print("Invalid task number. Please try again.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

################################################################################################################
# due date

lisst = []

# Function to get the due time
def due_date():
    # Function to check if the date is in the correct format
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%M-%d")
            return True
        except ValueError:
            return False

    flag = True
    while flag:
        
        
        due_date_str = input("Please, Enter the due date for the task in this format (YYYY-MM-DD): ")

        # Check if the date is in the correct format
        if not is_valid_date(due_date_str):
            print("Invalid date format.")
        else:
            # Convert the due date string to a datetime object
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

            # Check if the due date is in the past
            if due_date < datetime.now():
                print("The due date is in the past, It should be a future date.")
            else:
                flag = False

    # Calculate the time remaining until the due date
    time_remaining = due_date - datetime.now()

    # Calculate the total number of seconds
    total_seconds = time_remaining.total_seconds()

    # Calculate the number of days and hours
    days = total_seconds // (24 * 60 * 60)
    hours = (total_seconds % (24 * 60 * 60)) // 3600

    # If there are more than 30 minutes remaining to the next hour, round up
    if (total_seconds % 3600) > 1800:
        hours += 1

    # If there are more than 12 hours remaining to the next day, round up
    if hours > 12:
        days += 1
        hours = 0

    lisst.append(days)
    lisst.append(hours)
    return lisst