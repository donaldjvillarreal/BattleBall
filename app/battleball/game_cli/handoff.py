'''
This program implements the ball handoff function between two players. 
'handoff' function is the main/only function of the program
'''

from game_pieces import game_piece
''' 
This function takes as input two game_piece objects. Their dices are rolled.	
If the dice are not the same, the handoff is successful and the the player
without the ball now has the ball and the player who had it loses it. If the
dice are the same the ball is fumbled and thwe resolve fumble function is used.
from game_pieces import game_piece
'''

def handoff(player1, player2):
	# test if the two players are instances of 'game_piece' class
	# if either one of them are not, exception is thrown by 'assert' function
	assert (isinstance(player1, game_piece)) and (isinstance(player2, game_piece))

	# roll the dice for both players
	result1 = player1.roll()
	result2 = player2.roll()

	if result1 != result2:
		if player1.has_ball and (not player2.has_ball):
			print 
			print 'rolling the dice ...'
			print 'toggling the ball ...'
			print
			player1.ball_toggle()
			player2.ball_toggle()

		elif player2.has_ball and (not player1.has_ball):
			print 
			print 'rolling the dice ...'
			print 'toggling the ball ...'
			print
			player1.ball_toggle()
			player2.ball_toggle()

	else:
		'''
	 	if results of dice rolls are same, 
		then resolve fumble fucntion is called,
		which is yet to be implemented.
		'''

