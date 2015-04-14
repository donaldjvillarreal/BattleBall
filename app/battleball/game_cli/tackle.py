'''
This the tackle function:
This function takes as input two game piece objects.
The function should roll the respective pieces die, 
compare which one is smaller, update the losing pieces 
is_injured attribute and return the losing piece.
'''

from game_pieces import game_piece

def tackle(player1, player2):
	# test if the two players are instances of 'game_pice' class
	# if either one of them are not, exception is thrown by 'assert'
	# function
	assert (isinstance(player1, game_piece)) and (isinstance(player2, game_piece))
	
	# roll the dice for both players
	result1 = player.roll()
	result2 = player.roll()
	
	# compare which die result is smaller
	if result1 < result2:
	




