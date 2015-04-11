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

