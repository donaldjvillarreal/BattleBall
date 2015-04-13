# This is the test code for the ball handoff function
# between two players: 'handoff.py'
# Test code is incomplete ... 

'''
#######uncomment this to print some command line test#######
############################################################
from game_pieces import game_piece
from handoff import handoff
import random

player1 = game_piece(6, 13, 'running back')
player2 = game_piece(20, 1, 'linemam 1')

# suppose player1 has the ball, and player2 doesn't
player1.ball_toggle()
print 'player1 has ball? ', player1.has_ball
print 'player2 has ball? ', player2.has_ball

# now test the handoff function
handoff(player1, player2)
print 'player1 has ball? ', player1.has_ball
print 'player2 has ball? ', player2.has_ball
'''

import unittest
from mock import Mock, patch
from handoff import handoff
from game_pieces import game_piece

class test_handoff(unittest.TestCase):
	
	def test_handoff_function(self):
		# instantiate two players
		player1 = game_piece(6, 13, 'running back')
		player2 = game_piece(20, 1, 'lineman 1')
		
		# both player shouldn't have ball by default
		self.assertEqual(0, player1.has_ball)
		self.assertEqual(0, palyer2.has_ball)

		# suppose player 1 has the ball, but player 2 doesn't
		player1.ball_toggle()
		self.assertEqual(1, player1.has_ball)
		
		# now, handoff the ball from player1 to player2
		handoff(player1, player2)
		
		# now, player2 should have the ball, player1 shouldn't
		# assuming the dices are rolled with different numbers
		self.assertEqual(0, player1.has_ball)
		self.assertEqual(1, player2.has_ball)
		

