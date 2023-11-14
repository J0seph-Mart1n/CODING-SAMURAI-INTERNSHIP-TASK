import os

main_task_list = []

#Function to add Tasks
def add_task():                                  
    title = input("Enter Title of Task: ")
    description = input("Enter Description of Task: ")
    status = input("Enter Status (Complete/Incomplete): ")
    task = {"Title":title, "Description":description, "Status":status}
    main_task_list.append(task)
    print("Task has been added")

#Function to Display task
def list_task():
    if len(main_task_list)==0:
        print("No Tasks to list!!")
    else:
        print("Task List:")
        for i, task in enumerate(main_task_list): 
            #Here enumerate function is used to count the no of tasks present in the main_task_list       
            print(f"Task ID: {i+1}, Title: {task['Title']}, Description: {task['Description']}, Status: {task['Status']}")

#Function to mark task as Incomplete/Complete
def mark_task():
    list_task()
    index = int(input("Enter the task number to mark as Complete/Incomplete: ")) - 1
    if index in range(0,len(main_task_list)):
        status = input("Enter Complete/Incomplete: ")
        main_task_list[index]["Status"] = status
        print("Task status updated successfully!")
    else:
        print("Invalid task number.")

#Function to delete a specific task
def delete_task():
    task_id = int(input("Enter task ID to delete: ")) - 1
    if task_id in range(0,len(main_task_list)):
        del main_task_list[task_id]
        print("Task deleted successfully.")
    else:
        print("Invalid task ID!")

#Function to save task to a file    
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in main_task_list:
            file.write(f"{task['Title']},{task['Description']},{task['Status']}\n")
    print("Tasks saved to file.")

#Function to load task to a file    
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                title, description, status = line.strip().split(',')
                main_task_list.append({"Title": title, "Description": description, "Status":status})
        print("Tasks loaded from file.")

#Main Function 
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete/Incompleted")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
