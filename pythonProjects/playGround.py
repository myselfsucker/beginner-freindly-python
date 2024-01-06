list_of_tasks = []


def main():
         print("Wellcome to my ToDo app!!!")
         while True:
                 print("press 1 to add tasks\n press 2 to see tasks\n press 3 to delete tasks.")
                 
                         
                 user_input=int(input('Enter a command: ')) 

                 if user_input==1:
                         while True:
                                 ask = input("Add a task: ")
                                 if not ask.isspace() and not ask.isdigit():
                                         addTask(ask)
                                         break
                                 print("Don't leave blank or enter an intiger!")
                 elif user_input==2:
                         if not list_of_tasks:
                                 print("there is no tasks yet.")
                         else:
                                 seeTasks(list_of_tasks)
                 elif user_input==3:
                         if not list_of_tasks:
                                 print("There is no tasks yet.")
                         else:
                                 seeTasks(list_of_tasks)
                                 askD=int(input("Which task you want to delete"))
                                 if 0<=askD<=len(list_of_tasks):
                                         
                                    deleteTask(askD)
                                 else:
                                         print("Invalid index")   
                         
                         
                         

def addTask(task:str):
        
        list_of_tasks.append(task)
        
        print('task has been added successfully.')
        

def seeTasks(tasks:list):
        for index, i in enumerate(tasks, start=1):
                print(f"{index}. {i}")


def deleteTask(task:int):
        task=task-1
        list_of_tasks.pop(task)
        




if __name__=="__main__":
        main()






