from sys import exit
import csv


def main():
        todo = ToDo()                                                                                          
        while True:
                
                print("""
----------------------------
1. see all tasks 
2. add item
3. delete item
4. mark as done 
----------------------------""")
                
                try:
                        
                        use_input = input('> ')
                        if use_input == '2':
                                adding = input('Add A task: ').lower()
                                adding1 = todo.add_item(adding)
                        elif use_input == '3':
                                print('\n--- Your To-Do List ---')
                                for index, task in enumerate(todo.todos, start=1):
                                        print(f'{index}. {task}')
                                deleting = int(input("delte a task: "))
                                deleting1 = todo.delete_item(deleting)
                        elif use_input == '1':
                                show = todo.show_all()
                        elif use_input == '4':
                                
                                print('\n--- Your To-Do List ---')
                                for index, task in enumerate(todo.todos, start=1):
                                        print(f'{index}. {task}')
                                deleting = int(input("mark as done: "))
                                deleting1 = todo.is_done(deleting)
                except KeyboardInterrupt:
                        exit()







class ToDo():
         def __init__(self):
                 
                 self.todos=list()
         def add_item(self, task: str):
                 self.todos.append(task)
                 print("Task has been added successufully.")


         def delete_item(self, index_task:int):
                 if not self.todos:
                        print('You dont have any tasks yet, so you cant delete them')
                 else:
                      


                        if 1 <= index_task <= len(self.todos):
                         
                                self.todos.pop(index_task - 1)
                                print('Task has been deleted succesfully')
                        else:
                                print('invalid index')


         def show_all(self):
                 counter = 1
                 if not self.todos:
                         print("no tasks found.")
                 else:
                         
                        for i in self.todos:
                                print(f"{counter}.{i}")
                                counter += 1
         def is_done(self, index_task:int):
                 index_task-=1
                 if not self.todos:
                        print('You dont have any tasks yet, so you cant delete them')
                 else:
                      


                        if 0 <= index_task <= len(self.todos):
                         
                                self.todos[index_task]=self.todos[index_task] + 'Done✅'
                                print('Task is complete!')
                        else:
                                print('invalid index')
        


if __name__=='__main__':

        main()