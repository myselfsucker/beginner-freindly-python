import random
chars = 'abcdefjhkABCDEFJHIKLMNOP!@#$%^1234567890'
while True:
    try:

        a = int(input("how many passes you want to get: "))
        if a >= 1:
            break
        else:
            print('You can have at least 1 passowrd!')
    except ValueError:
        print("enter an intiger!")    
while True:
    try:
        lenth = int(input("lenth of your passowrd (at least 7 chars): "))
        if lenth >= 7:
            break
        else:
            print("at least 7 chars")
    except ValueError:
        print('enter an intiger!')

print('here are your passwords')
for i in range(a):
    passwords = ''
    for h in range(lenth):
        passwords += random.choice(chars)
    print(f'{i + 1}.{passwords}')

                                




