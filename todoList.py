class TodoList(): 
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
        print(f'\'{task.description}\' added to list!')
        return task

    def show_list(self):
        print('This is your To-Do list:')
        for task in self.task_list:
            print(f'-{task.description} - {task.due_date}')
        
class Task():
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

todo_list = TodoList()
exercise = Task('Exercise', 'Today')
taxes = Task('File your taxes', 'April')
shopping = Task('Go shopping', 'Sunday')

todo_list.add_task(exercise)
todo_list.add_task(taxes)
todo_list.add_task(shopping)
print()

todo_list.show_list()