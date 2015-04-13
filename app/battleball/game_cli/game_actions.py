'''
This file contains  function necessary to have
player turns and game setup
'''
import battle_board as bb
import game_pieces as gp

def prompt_place_piece(piece, piece_index, gameboard, team):
    '''
    prompts user to place a piece and ensures it can be placed
    at the ive x y location
    '''
    while True:
        print 'Place your ' + piece.name

        x = int(raw_input('Row: '))
        y = int(raw_input('Column: '))
        y2 = -1

        if piece.name == 'heavy tackle':
            y2 = y + 1

        # Ensure input is correct
        if (team == 'home' and (x < 1 or x > 6)):
            print 'Row out of range'
            continue
        elif (team =='away' and (x < 26 or x > 31)):
            print 'Row out of range'
            continue
        if (y < 0 or y > 15 or y2 > 15):
            print 'Column our of range'
            continue
        if(x % 2 == 0 and y > 14 and y2 > 14):
            print 'Column out of range'
            continue
        if not bb.empty_space(gameboard, x,y):
            print 'Space is occupied'
            continue

        if (piece.name == 'heavy tackle' and not bb.empty_space(gameboard, x, y2)):
            print 'Space is occunpied'
            continue
        else:
            bb.place_piece(piece_index, (x,y), gameboard)
            piece.place_on_board(x,y)
            if piece.name == 'heavy tackle':
                bb.place_piece(piece_index, (x,y2), gameboard)
            break

def choose_piece_to_move(piece_dictionary, team):
    '''
    This function lets a player chose a uninjured piece to move.
    It returns the chosen piece.
    '''
    while True:
        available_pieces = []
        for piece in piece_dictionary[team]:
            if (not piece.injured):
                available_pieces.append(piece)

        print "You can move one of the following pieces."
        for piece in available_pieces:
            print piece.name
        chosen_one = raw_input("Please select one: ")

        for piece in available_pieces:
            if (piece.name == chosen_one):
                piece_index = piece_dictionary[team].index(piece)
                return piece_index
        else:
            print "Invalid input"

def prompt_move_piece(piece, piece_index, rolled_value, score, gameboard, team):
    '''
    Prompts the player to choose a location based on
    the rolled value
    '''
    while True:
        print 'Choose a location for ' + piece.name

        x = int(raw_input('Row: '))
        y = int(raw_input('Column: '))
        y2 = -1

        if piece.name == 'heavy tackle':
            y2 = y + 1

        # Ensure input is correct
        within_roll = gp.check_movement(piece, rolled_value, (x,y))
        if (not within_roll):
            print "You can't move that far"
            continue
        if (y < 0 or y > 15 or y2 > 15):
            print 'Column out of range'
            continue
        if(x % 2 == 0 and y > 14 and y2 > 14):
            print 'Column out of range'
            continue
        if not bb.empty_space(gameboard, x,y):
            print 'Space is occupied'
            continue

        if (piece.name == 'heavy tackle' and not bb.empty_space(gameboard, x, y2)):
            print 'Space is occunpied'
            continue
        else:
            # empty old position
            old_position = piece.position
            gameboard[old_position['xpos']][old_position['ypos']] = 'E'
            if piece.name == 'heavy tackle':
                gameboard[old_position['xpos']][old_position['ypos2']] = 'E'

            # check for ball
            if (gameboard[x][y] == 'B'):
                piece.has_ball = True

            # place piece
            bb.place_piece(piece_index, (x,y), gameboard)
            piece.place_on_board(x,y)

            # heavy tackle
            if piece.name == 'heavy tackle':
                if (gameboard[x][y2] == 'B'):
                    piece.has_ball = True
                bb.place_piece(piece_index, (x,y2), gameboard)

            # check if touchdown
            if (touchdown(piece, (x,y), team)):
                score[team] += 1
                return True
            else:
                return False

def touchdown(piece, to_location, team):

    '''
    This function checks if a piece with the ball enters
    the endzone
    '''

    if (piece.has_ball):
        if (team == 'home'):
            row = to_location[0]
            if (row == 31 or row == 32):
                piece.has_ball = False
                print 'The ' + team + ' has scored a touchdown'
                return True
        else:
            row = to_location[0]
            if (row == 0 or row == 1):
                piece.has_ball = False
                print 'The ' + team + ' has scored a touchdown'
                return True
    else:
        return False
