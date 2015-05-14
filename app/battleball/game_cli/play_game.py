'''
inline full gameplay
'''
import battleball.game_cli.battle_board as bb
import battleball.game_cli.game_pieces as gp
#import battleball.game_cli.game_actions as ga

# Set up initial board and pieces
PDICTIONARY = gp.instatiate_pieces()
TEAMS = ['home', 'away']
SCORES = {'home': 0, 'away': 0}
GAMEBOARD = bb.create_gameboard()

while not (SCORES['home'] == 2 or SCORES['away'] == 2):

    for team in TEAMS:
        print team + ' team, place your pieces behind the 20 yard line'
        for piece_index in range(len(PDICTIONARY[team])):

            piece = PDICTIONARY[team][piece_index]
            #ga.prompt_place_piece(piece, piece_index, GAMEBOARD, team)
            bb.print_board(GAMEBOARD)

    SCORED = False
    while not SCORED:
        for team in TEAMS:
            print team + ' team, choose a piece to move'
            #piece_index = ga.choose_piece_to_move(PDICTIONARY, team)
            piece = PDICTIONARY[team][piece_index]
            rolled_value = piece.roll()
            print 'You rolled a ' + str(rolled_value) + ' for ' + piece.name
            #SCORED = ga.prompt_move_piece(piece, piece_index, rolled_value, SCORES,
                                           #GAMEBOARD, team)
            print 'Home: ' + str(SCORES['home']) + ' Away: ' + str(SCORES['away'])
            bb.print_board(GAMEBOARD)
            if SCORED:
                break

for team, score in SCORES.iteritems():
    if score == 2:
        print team + ' team has won'
