import random

class game_piece:
    def __init__(self, roll_size, psize, name):
        self.has_ball = 0
        self.injured = 0
        self.position = {'xpos':-1, 'ypos':-1}
        if(psize==2):
            self.position['ypos2'] = -2
        self.roll_size = roll_size
        self.psize = psize
        self.name = name

    def ball_toggle(self):
        self.has_ball = not self.has_ball

    def place_on_board(self, x, y):
        self.position['xpos'] = x
        self.position['ypos'] = y
        if(self.psize==2):
            self.position['ypos2'] = y+1

    def move(self, x, y):
        self.position['xpos'] = self.position['xpos']+x
        self.position['ypos'] = self.position['ypos']+y
        if(self.psize==2):
            self.position['ypos2'] = self.position['ypos2']+y

    def injury(self, severity):
        self.injured = severity

    def roll(self):
        return random.randint(1,self.roll_size)


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
    player_dict = {'home': [ heavy_tackle_h, tackle_h, lineman1_h, lineman2_h, 
                             linebacker1_h, linebacker2_h, safety1_h, safety2_h, 
                             running_back1_h, running_back2_h, running_back3_h],

                   'away': [ heavy_tackle_a, tackle_a, lineman1_a, lineman2_a, 
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

    pass
