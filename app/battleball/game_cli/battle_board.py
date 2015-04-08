"""
This file contains functions related to the gameboard
"""

def create_gameboard():
    '''
    Creates a list of lists that represent the rows of a game board
    The board has 33 rows. The first and last rows are the endzones
    and have 16 spaces.The other 31 rows are the field made up of
    alternating rows of length 15 and 16
    '''
    gameboard = []

    #creates first endzone
    gameboard.append(['0']*16)

    #create field
    for i in range(0, 31):
        if i == 15:
            row = ['0']*15
            row[7] = '1'
            gameboard.append(row)
        elif i%2 == 0:
            gameboard.append(['0']*16)
        else:
            gameboard.append(['0']*15)

    #creates second endzone
    gameboard.append(['0']*16)

    return gameboard
    
def print_board(gameboard):
    '''
    This function takes the current game board and prints it neatly to 
    the console
    '''
    print " ".join(gameboard[0])

    for i in range(1, 32):
        if i%2 == 1:
            print " ".join(gameboard[i])
        else:
            print " " +" ".join(gameboard[i])

    print " ".join(gameboard[32])
