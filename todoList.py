class Task():

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date




class TodoList():
    
    def __init__(self):
        # self = self
        pass

    def add_task(self, task):
        print(task)
        pass


exercise = Task('Exercise', 'Today')
taxes = Task('File your taxes', 'April')
shopping = Task('Go shopping', 'Sunday')

print(exercise)
print(taxes)
print(shopping)
print()


todo_list = TodoList()
todo_list.add_task(exercise)