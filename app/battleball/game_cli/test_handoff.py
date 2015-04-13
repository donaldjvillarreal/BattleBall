# This is the test code for the ball handoff function
# between two players: 'handoff.py'
# Test code is incomplete ... 

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

