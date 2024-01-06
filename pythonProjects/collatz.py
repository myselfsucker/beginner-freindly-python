def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:     
        result = 3 * number + 1
    print(result)
    return result

def main():
    try:
        user_input = int(input("Enter an integer: "))
        while user_input != 1:
             user_input = collatz(user_input)
    except ValueError:
        print("You must enter an integer.")
main()