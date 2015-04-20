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

def place_piece(piece_index, location, gameboard):
    '''
    This function updates gameboard by placing a piece
    objects index and the location provided

    location is a tuple (col,row)
    '''
    col = location[0]
    row = location[1]

    if empty_space(gameboard, col, row):
        gameboard[col][row] = str(piece_index)
        return True
    else:
        return False

def empty_space(gameboard, col, row):
    '''
    This function checks if a given space is taken up by another piece
    '''

    if gameboard[col][row] == 'E' or gameboard[col][row] == 'B':
        return True
    else:
        return False

def resolve_fumble(location, gameboard):
    '''
    This function updates gameboard with the ball after
    a fumble occurs

    location is a tuple (col,row)
    '''
    col = location[0]
    row = location[1]

    if gameboard[col][row] != 'E':
        return False
    else:
        gameboard[col][row] = 'B'
        return True

def check_adjacent(gameboard, col, row):
    '''
    This function will check the neighboring squares
    and return a dictionary of it's neighbors
    '''
    occupied = {}
    occupied['l'] = gameboard[col][row-1]
    occupied['r'] = gameboard[col][row+1]
    if 1 < col < 31:
        if col%2 == 0:
            occupied['ul'] = gameboard[col-1][row]
            occupied['ur'] = gameboard[col-1][row+1]
            occupied['dl'] = gameboard[col+1][row]
            occupied['dr'] = gameboard[col+1][row+1]
        else:
            occupied['ul'] = gameboard[col-1][row-1]
            occupied['ur'] = gameboard[col-1][row]
            occupied['dl'] = gameboard[col+1][row-1]
            occupied['dr'] = gameboard[col+1][row]
    return occupied

def move(gameboard, p_index, start, end):
    '''
    This function will move a piece from col1, row1 to col2, row2
    '''
    gameboard[start.col][start.row] = 'E'
    gameboard[end.col][end.row] = p_index
    if p_index == 0:
        gameboard[start.col][start.row+1] = 'E'
        gameboard[end.col][end.row+1] = p_index
