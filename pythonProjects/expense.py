def main():
        expense = Expense()
        expense.category = {}
        print("Welcome")
        while True:
                

                while True:
                           
                  if expense.category:
                           for index, key in enumerate(expense.category, start=1):
                                    print(index, key)
                           category_choice = int(input("Choose the category: ")) 
                           if 0<=category_choice<=len(expense.category):
                                    
                                                      
                                             category_expense = int(input('Enter the expense: '))
                                             if category_expense.isdecimal():
                                                      expense.category[category_choice]+=category_expense
                                             else:
                                                      print('Enter an intiger.')
                  else:
                           print("You don't any categories, so create one")
                           create_category = input("Enter the name: ")
                           expense.category[create_category]= int()
                           break      

                                     
                          



class Expense():
         def __init__(self):
                 
                 self.category = {}
                 self.expen = int()


if __name__=='__main__':
        main()