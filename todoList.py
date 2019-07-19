class TodoList(): 
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
        return task
        
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

for task in todo_list.task_list:
    print(f'{task.description} - {task.due_date}')