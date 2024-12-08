todos = []        

# Add a task
def add_todo():
    add_input = input('\nWhat task would like to add?: ')
    todos.append(add_input)
    print(f'Todo "{add_input}" added!')

# View Tasks
def view_todos():
    if len(todos) == 0:
        print('No todos to view!')
    else:
        print('\nTasks todo!')
        for index, task in enumerate(todos):
            print(f'{index + 1}. {task}')

# Delete Tasks
def delete_todo():
    view_todos()
    try:
        delete_input = int(input('Please select the number of the todo you would like to delete!: '))
        if delete_input >= 0 and delete_input < len(todos):
            todos.pop(delete_input - 1) 
            print(f'Todo {delete_input} has been removed!')
        else:
            print('Todo was not found!')
            view_todos()
    except:
        print('Invalid selection.')

def begin_application():
    
    
    
    print('Welcome to your personal todo application \n')
    
    while True:
         
        print('\nPlease select one of the following \n'
              '-----------------------------------------')
        print('1. Add Task \n'
              '2. Delete Task \n'
              '3. View Tasks \n'
              '4. Quit Application \n')
        
        user_selection = int(input('What would you like to do?: \n'))
        
        if user_selection == 1:
            add_todo()
            print(todos)
        elif user_selection == 2:
            delete_todo()
        elif user_selection == 3:
            view_todos()
        elif user_selection == 4:
            break
        else: 
            print('Please select one of the options provided')
            continue

begin_application()