import random, sys
losses = 0
wins = 0
ties = 0



while True: 
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit() 
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break 
        print('Type one of r, p, s, or q.')
    if playerMove == 'r':
        print('rock versus...')
    elif playerMove == 'p':
        print('paper vresus...')
    elif playerMove == 's':
        print('scissors versus...')
    

    randomNumber = random.randint(1, 3)


    if randomNumber == 1:
        computer_move = 'r'
        print('rock')
    elif randomNumber == 2:
        computer_move = 'p'
        print('paper')
    elif randomNumber == 3:
        computer_move = 's'
        print("sicossors")
    if playerMove == computer_move:
        print('it is a tie')
        ties += 1 
    elif playerMove == 'r' and computer_move == 'p':
        print("you lose!")
        losses += 1 
    elif playerMove == 's' and computer_move == 'p':
        print('you win!')
        wins += 1 
    elif playerMove == 's' and computer_move == 'r':
        print('you lose! ')
        losses += 1 
    elif playerMove == 'p' and computer_move == 's':
        print('you lose')
        losses += 1 
    elif playerMove == 'p' and computer_move == 'r':
        print('you win!')
        wins += 1
    elif playerMove == 'r' and computer_move == 's':
        print('you win!')
        wins += 1 

    if wins - losses == -3:
        print('you lost 3 times in a row!')
        sys.exit()

