'''
This file controls the game_piece objects, which are placed on the board.
'''
import random

class game_piece(object):
    '''
    Below is the game_piece class which contains it's own roll, move, place_on_board
    and injury functions.
    The board has it's own class as well
    '''
    def __init__(self, roll_size, psize, name):
        self.has_ball = False
        self.injured = 0
        self.position = {'xpos':-1, 'ypos':-1}
        if psize == 2:
            self.position['ypos2'] = -2
        self.roll_size = roll_size
        self.psize = psize
        self.name = name

    def ball_toggle(self):
        '''
        toggles has_ball
        '''
        self.has_ball = not self.has_ball

    def place_on_board(self, col, row):
        '''
        starting position on the board
        '''
        self.position['xpos'] = col
        self.position['ypos'] = row
        if self.psize == 2:
            self.position['ypos2'] = row+1

    def move(self, col, row):
        '''
        incremental move on board
        '''
        self.position['xpos'] = self.position['xpos']+col
        self.position['ypos'] = self.position['ypos']+row
        if self.psize == 2:
            self.position['ypos2'] = self.position['ypos2']+row

    def injury(self, severity):
        '''
        injury of 0 = no injury, injury of 1 = out for game
        injury of 2 = outpermanenty
        '''
        self.injured = severity

    def roll(self):
        '''     rolls dice depending on type of player      '''
        return random.randint(1, self.roll_size)

def create_piece():
    '''     create piece for short board        '''
    running_back = game_piece(20, 1, 'running back')
    return running_back

def instatiate_pieces():
    '''
    This function returns a dictionary containing the initial game pieces

    pieces = {home: [],
              away: []}

    and the indicies of the list are as follow:

    0        - heavy tackle
    1        - tackle
    2,3      - linemen
    4,5      - linebacker
    6,7      - safety
    8, 9, 10 - running back
    '''

    #instatiate pieces
    heavy_tackle_h = game_piece(6, 2, 'heavy tackle')
    tackle_h = game_piece(6, 1, 'tackle')
    lineman1_h = game_piece(8, 1, 'lineman 1')
    lineman2_h = game_piece(8, 1, 'lineman 2')
    linebacker1_h = game_piece(10, 1, 'linebacker 1')
    linebacker2_h = game_piece(10, 1, 'linebacker 2')
    safety1_h = game_piece(12, 1, 'safety 1')
    safety2_h = game_piece(12, 1, 'safety 2')
    running_back1_h = game_piece(20, 1, 'running back 1')
    running_back2_h = game_piece(20, 1, 'running back 2')
    running_back3_h = game_piece(20, 1, 'running back 3')

    heavy_tackle_a = game_piece(6, 2, 'heavy tackle')
    tackle_a = game_piece(6, 1, 'tackle')
    lineman1_a = game_piece(8, 1, 'lineman 1')
    lineman2_a = game_piece(8, 1, 'lineman 2')
    linebacker1_a = game_piece(10, 1, 'linebacker 1')
    linebacker2_a = game_piece(10, 1, 'linebacker 2')
    safety1_a = game_piece(12, 1, 'safety 1')
    safety2_a = game_piece(12, 1, 'safety 2')
    running_back1_a = game_piece(20, 1, 'running back 1')
    running_back2_a = game_piece(20, 1, 'running back 2')
    running_back3_a = game_piece(20, 1, 'running back 3')

    #place into dictionary
    player_dict = {'home': [heavy_tackle_h, tackle_h, lineman1_h, lineman2_h,
                            linebacker1_h, linebacker2_h, safety1_h, safety2_h,
                            running_back1_h, running_back2_h, running_back3_h],

                   'away': [heavy_tackle_a, tackle_a, lineman1_a, lineman2_a,
                            linebacker1_a, linebacker2_a, safety1_a, safety2_a,
                            running_back1_a, running_back2_a, running_back3_a]}

    return player_dict

def check_movement(piece, roll_value, to_position):
    '''
    This function is called when a player picks
    a location to move a piece

    It returns true if the move is legal and false
    otherwise
    '''

    from_position = piece.position
    change_in_x = abs(to_position[0] - from_position['xpos'])
    change_in_y = abs(to_position[1] - from_position['ypos'])
    total = change_in_x + change_in_y

    if total > roll_value:
        return False
    else:
        return True

def touchdown(piece, to_location, team):

    '''
    This function checks if a piece with the ball enters
    the endzone
    '''

    if piece.has_ball:
        if team == 'home':
            row = to_location[0]
            if row == 31 or row == 32:
                piece.has_ball = False
                print 'The ' + team + ' has scored a touchdown'
                return True
        else:
            row = to_location[0]
            if row == 0 or row == 1:
                piece.has_ball = False
                print 'The ' + team + ' has scored a touchdown'
                return True
    else:
        return False

def calculate_move(piece, move):
    '''
    This function will calculate a pieces new position after
    a move
    '''

    current_location = piece.position
    row = current_location['xpos']
    column = current_location['ypos']
    newMove = {}
    if row % 2 == 0:
        if move == 'ul':
            row = row - 1
        elif move == 'ur':
            row = row -1
            column = column + 1
        elif move == 'l':
            column = column - 1
        elif move == 'r':
            column = column + 1
        elif move == 'dl':
            row = row + 1
        else:
            row = row + 1
            column = column + 1
    else:
        if move == 'ul':
            row = row - 1
            column = column - 1
        elif move == 'ur':
            row = row -1
        elif move == 'l':
            column = column - 1
        elif move == 'r':
            column = column + 1
        elif move == 'dl':
            row = row + 1
            column = column - 1
        else:
            row = row + 1
    newMove['row'] = row
    newMove['col'] = column
    return newMove

def check_move(piece, position, gameboard):
    '''
    This function will check to see the position is valid
    '''

    col = position[0]
    row = position[1]
    row2 = row + 1

    if col < 0 or col > 32:
        print 'Row out of range'
        return False
    if piece.name == 'heavy tackle':
        if  row < 0 or row > 15 or row2 > 15:
            print 'Column out of range'
            return False
        if col % 2 == 0 and row > 14 and row2 > 14:
            print 'Column out of range'
            return False
    else:
        if row < 0 or row > 15:
            print 'Column out of range'
            return False
        if col % 2 == 0 and row > 14:
            print 'Column out of range'
            return False
    if not (gameboard[col][row] == 'E' or gameboard[col][row] == 'B'):
        print 'Space is occupied'
        return False
    if (piece.name == 'heavy tackle' and
            not (gameboard[col][row] == 'E' or gameboard[col][row] == 'B')):
        print 'Space is occupied'
        return False
    else:
        return True

