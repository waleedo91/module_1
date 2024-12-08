# TODO Create a main function to run the program that will take a users input
# TODO Be sure to add error handling for each of the functions to notify user the error. 
        # Alert the user if they provide invalid input
        # Alert the user if there are no tasks to view
        # Alert the user if they try to delete a task that doesn't exist
        # Alert the user if they select an option on the main menu that doesn't exist
        
# TODO Create an empty list to enter todos
todos = ['task']        

        
# TODO Create 3 separate functions to ADD, VIEW and REMOVE a todo

# Add a task
def add_tasks(task):
    for t in todos:
        if t.lower() == task.lower():
            print(f'{task} already exists. Please enter a new task!')
        else:
            return todos.append(task.lower())

# View Tasks
def view_tasks():
    for task in todos:
        print(task)

# Delete Tasks
def delete_task(task):
    for t in todos:
        if task.lower() == t:
            return todos.remove(t)


def begin_application():
    
    print('Welcome to your personal todo application \n')
    
    while True:
        print('Please select one of the following \n')
        print('1. Add Task \n'
              '2. Delete Task \n'
              '3. View Tasks \n'
              '4. Quit Application \n')
        
        user_selection = int(input('What would you like to do?: '))
        
        if user_selection == 1:
            add_input = input('\nWhat task would like to add?: ')
            add_tasks(add_input)
            print(todos)
        elif user_selection == 2:
            break
        elif user_selection == 3:
            break
        elif user_selection == 4:
            break
        else: 
            print('Please select one of the options provided')
            continue

begin_application()