from random import choice 
from sys import argv

chars = 'abcdefjhiklmno123457890!@#%$^&**()[]'

password = ''
lenth = int(argv[1])



for i in range(lenth):
         char = choice(chars)
         password += char

print(password)






