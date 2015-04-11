import battle_board as bb
import game_pieces as gp
import game_actions as ga

# Set up initial board and pieces
gameboard = bb.create_gameboard()
piece_dictionary = gp.instatiate_pieces()


for team in ['home','away']:
    print team + ' team, place your pieces behind the 20 yard line'
    for piece_index in range(len(piece_dictionary[team])):
        
        piece = piece_dictionary[team][piece_index]
        ga.prompt_place_piece(piece, piece_index, gameboard, team)
        bb.print_board(gameboard)