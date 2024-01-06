import random 
secret = 23
lower_bound = int(input('lower bound: '))
higher_bound = int(input("higher_bound: "))
while True:
    guess = random.randint(lower_bound, higher_bound)
    print(guess)   
    if guess > secret:
        print("Wrong! it is less that that")
        higher_bound = guess
    elif guess < secret:
        print("Wrong! it is greater than that.")
        lower_bound = guess

    elif guess == secret:
        print("You win!")
        break 
