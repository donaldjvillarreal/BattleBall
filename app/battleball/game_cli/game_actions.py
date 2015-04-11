'''
This file contains  function necessary to have
player turns and game setup
'''
import battle_board as bb
import game_pieces as gp

def prompt_place_piece(piece, piece_index, gameboard):
    '''
    prompts user to place a piece and ensures it can be placed
    at the ive x y location
    '''
    while True:
    	print 'Place your ' + piece.name
    	x = int(raw_input('Row: '))
    	y = int(raw_input('Column: '))

    	# Ensure input is correct
    	if (x < 0 or x > 32):
    		print 'Row out of range'
    		continue
    	if (y < 0 or y > 15):
    		print 'Column our of range'
    		continue
    	if(x % 2 == 0 and y > 14):
    		print 'Column out of range'
    		continue
    	if not bb.empty_space(gameboard, x,y):
    		print 'Space is occupied'
    		continue
    	else:
    		bb.place_piece(piece_index, (x,y), gameboard)
    		piece.place_on_board(x,y)
    		break

