s = 1000


def find7(sucker: int):
         

         
         while sucker > 990:


                  if sucker % 7 == 0:
                           print(sucker)
                           return sucker
                           
                  else:
                          print('bomadi!')
                          sucker-=1

find7(s)
