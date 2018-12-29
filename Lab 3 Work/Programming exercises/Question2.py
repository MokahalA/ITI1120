def rps(player1choice,player2choice):
    '''(str,str) --> int
Given a string R,S, or P. It prints an integer 1 if player 1 wins, or -1 if
player 2 wins, and it prints 0 if the result is a tie. '''
    
    'R'>'S'
    'S'>'P'
    'P'>'R'
    
    if player1choice > player2choice:
        print(1)
    elif player1choice < player2choice:
        print(-1)
    else:
        print(0)

