



t = ('listening: ', 'reading: ', "speaking: ", 'writing: ' )
def main():
                
        summa = 0
        while True:
                try:

                        for i in t:
                                
                                try:
                                        ask = float(input(i))
                                
                                        
                                        summa += ask 
                                
                                        print('enter an intiger not a string!')
                                except ValueError:
                                        print("enter an int or float!")
                                        break
                except KeyboardInterrupt:
                        print("you stopped the programm")
                        break


                if summa:

                        score = str(summa // 4) 

                        print(f' your overall score: {score}')



def rounder(somep: str):
        
        if somep[somep.index('.'):] == 'uuu':
                pass


main()