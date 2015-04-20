'''
This file contains  functions that create
the game file used by the Game
'''
import battle_board as bb
import game_pieces as gp
import json

def create_game_file(game_id):
    '''
    This function creates a file called <id>_board.json
    which maintains the state of the board
    '''

    # Create board
    board = bb.create_gameboard()

    # create two pieces for board
    home_piece = gp.create_piece()
    away_piece = gp.create_piece()

    game_dict = { 'game' : {
                  'board' : board,
                  'home' : vars(home_piece),
                  'away' : vars(away_piece)
                  }
                }

    game_json = json.dumps(game_dict)
    filename = str(game_id) + '_board.json'
    with open(filename, 'w') as f:
        f.write(game_json)

    return filename

print type(create_game_file(1))