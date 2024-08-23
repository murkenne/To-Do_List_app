'''
Project requirements:

1. User Interface (UI):
-Create a command-line interface(CLI) for the To-Do List Application.
-Display a welcoming message and a menu with the following options:
  `Welcome to the To-Do List App!
  Menu:
  1. Add a task
  2. View tasks
  3. Mark a task as complete
  4. Delete a task
  5. Quit`
'''

tasks = []


def add_task():
    # Add a new task to the to-do list.
    task_title = input("Enter a new task: ")
    task = {"title":task_title, "status": "Incomplete"}
    tasks.append(task)
    print("Task added successfully.") 
    
def view_tasks():
    try:
        # View the tasks in the to-do list.
        if len(tasks) == 0:
            print("No tasks.")
        else:
            print("List of tasks:")
            for i, task in enumerate(tasks):
                print(f'{i + 1}. {task["title"]} - {task["status"]}')
    
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")
    
    finally:
        print("Completed viewing tasks.")

            
def delete_task():
    # Delete a task from the to-do list.
    if len(tasks) == 0:
        print("no task to delete.")
    else: 
        print('Task:') 
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} - {task['status']}")
        choice = int(input('Enter the task number to delete:'))
        
        if 0 < choice <= len(tasks):
            del tasks[choice -1]
            print('Task deleted successfully.')
        else:
            print("Invalid task number.")
            
            
def complete_task():
    # Mark a task as complete:
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
    else:
        print('Task:')
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} - {task['status']}")
        
        try:
            choice = int(input('Enter the task number to mark as complete: '))
            
            if 0 < choice <= len(tasks):
                tasks[choice - 1]['status'] = "Complete"
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        finally:
            print("Completed task operation.")


def main():
    # Run the command-line to-do list application
    while True:
        print("    Menu    ")
        print("1. Add task")
        print("2. view task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Quit")
        
        try:
                
            choice = int(input("Enter your choice:"))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                complete_task()
            elif choice == 5:
                print("Thank you for using the To-Do-List App.")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        

if __name__ == "__main__":
    main()
