# TODO Create a main function to run the program that will take a users input
# TODO Be sure to add error handling for each of the functions to notify user the error. 
        # Alert the user if they provide invalid input
        # Alert the user if there are no tasks to view
        # Alert the user if they try to delete a task that doesn't exist
        # Alert the user if they select an option on the main menu that doesn't exist
        
# TODO Create an empty list to enter todos
todos = []        

        
# TODO Create 3 separate functions to ADD, VIEW and REMOVE a todo

# Add a task
def add_tasks(task):
    return todos.append(task)

# View Tasks
def view_tasks():
    for task in todos:
        print(task)
    