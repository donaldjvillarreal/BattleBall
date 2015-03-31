"""
This program generates a json object that contains the initial
state of the gameboard without pieces on it
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
    gameboard.append([0]*16)

    #create field
    for i in range(0, 31):
        if i%2 == 0:
            gameboard.append([0]*16)
        else:
            gameboard.append([0]*15)

    #creates second endzone
    gameboard.append([0]*16)

    return gameboard
    