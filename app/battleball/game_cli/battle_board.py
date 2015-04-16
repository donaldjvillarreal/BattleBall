"""
This file contains functions related to the gameboard
"""

def create_gameboard():
    '''
    Creates a list of lists that represent the rows of a game board
    The board has 13 rows. The first and last rows are the endzones
    and have 11 spaces.The other 31 rows are the field made up of
    alternating rows of length 6 and 5
    '''
    gameboard = []

    #creates first endzone
    gameboard.append(['E']*6)

    #create field
    for i in range(0, 11):
        if i == 5:
            row = ['E']*5
            row[2] = 'B'
            gameboard.append(row)
        elif i%2 == 0:
            gameboard.append(['E']*6)
        else:
            gameboard.append(['E']*5)

    #creates second endzone
    gameboard.append(['E']*6)

    return gameboard
    
def print_board(gameboard):
    '''
    This function takes the current game board and prints it neatly to 
    the console
    '''
    print '      Home       '
    print " ".join(gameboard[0])

    for i in range(1, 12):
        if i%2 == 1:
            print " ".join(gameboard[i])
        else:
            print " " +" ".join(gameboard[i])

    print " ".join(gameboard[12])
    print '      Away       '

def empty_space(gameboard, x, y):
    '''
    This function checks if a given space is taken up by another piece
    '''

    if (gameboard[x][y] == 'E' or gameboard[x][y] == 'B'):
        return True
    else:
        return False

def place_piece(piece_index, location, gameboard):
    '''
    This function updates gameboard by placing a piece
    objects index and the location provided

    location is a tuple (x,y)
    '''
    x = location[0]
    y = location[1]

    if empty_space(gameboard, x, y):
        gameboard[x][y]  = str(piece_index)
        return True
    else:
        return False

def resolve_fumble(location, gameboard):
    '''
    This function updates gameboard with the ball after
    a fumble occurs

    location is a tuple (x,y)
    '''
    x = location[0]
    y = location[1]
    
    if(gameboard[x][y] != 'E'):
        return False
    else:
        gameboard[x][y] = 'B'
        return True

def check_adjacent(gameboard, x, y):
    occupied = {}
    occupied['l'] = gameboard[x][y-1]
    occupied['r'] = gameboard[x][y+1]
    if(1 < x < 31):
        if(x%2 == 0):
            occupied['ul'] = gameboard[x-1][y]
            occupied['ur'] = gameboard[x-1][y+1]
            occupied['dl'] = gameboard[x+1][y]
            occupied['dr'] = gameboard[x+1][y+1]
        else:
            occupied['ul'] = gameboard[x-1][y-1]
            occupied['ur'] = gameboard[x-1][y]
            occupied['dl'] = gameboard[x+1][y-1]
            occupied['dr'] = gameboard[x+1][y]
    return occupied

def move(gameboard, p_index, x1, y1, x2, y2):
    gameboard[x1][y1] = 'E'
    gameboard[x2][y2] = p_index
    if(p_index==0):
        gameboard[x1][y1+1] = 'E'
        gameboard[x2][y2+1] = p_index