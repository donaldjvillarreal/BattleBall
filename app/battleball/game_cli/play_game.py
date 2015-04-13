import battle_board as bb
import game_pieces as gp
import game_actions as ga

# Set up initial board and pieces
piece_dictionary = gp.instatiate_pieces()
teams = ['home', 'away']
scores = {'home': 0, 'away': 0}


while (not (scores['home'] == 2 or scores['away'] == 2)):

    gameboard = bb.create_gameboard()

    for team in ['home','away']:
        print team + ' team, place your pieces behind the 20 yard line'
        for piece_index in range(len(piece_dictionary[team])):
            
            piece = piece_dictionary[team][piece_index]
            ga.prompt_place_piece(piece, piece_index, gameboard, team)
            bb.print_board(gameboard)

    scored = False
    while (not scored):
        for team in teams:
            print team + ' team, choose a piece to move'
            piece_index = ga.choose_piece_to_move(piece_dictionary, team)
            piece = piece_dictionary[team][piece_index]
            rolled_value = piece.roll()
            print 'You rolled a ' + str(rolled_value) + ' for ' + piece.name
            scored = ga.prompt_move_piece(piece, piece_index,
                    rolled_value, scores, gameboard, team)
            print 'Home: ' + str(scores['home']) + ' Away: ' + str(scores['away'])
            bb.print_board(gameboard)
            if (scored):
                break

for team, score in scores.iteritems():
    if (score == 2):
        print team + ' team has won'
