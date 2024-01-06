import random
print('enter a range and i will think of a number in it: ')
try:

    lowestBound = int(input('enter the lowestbound: '))
    highestBound = int(input('enter the highestbound: '))
except ValueError:
    print("enter an intiger")
chances = 3
wrongAnswers = 0
while chances > wrongAnswers:
    guessedNumber = random.randint(lowestBound, highestBound)
    try:
            
        guessTheNumber = int(input("guess the number: "))
        if guessTheNumber > guessedNumber:
            print('you guessed a little  bit higher')
        elif guessTheNumber < guessedNumber:
            print('you guessed a little bit less')
        elif guessTheNumber == guessedNumber:
            print('you are right')
            break
        
        chances -= 1
        print('you have ' + str(chances) + ' chances left')
        
    except ValueError:
        print("enter an int")



