'''
This is the unittest code for the ball handoff function between
two players which is in source file called 'handoff.py'.
To handover the ball from one player to another, the handoff
function must be used. Each player's dice is rolled, and if
the resulting number is different, then player A passes the
ball to player B; otherwise, resolve fumble function is called.
'''

import unittest
from battleball.game_cli.handoff import handoff
from battleball.game_cli.game_pieces import game_piece

class TESTHANDOFF(unittest.TestCase):
    '''
    Two instances of game piece (player) are created. Each with differnt roll size (dice) and
    position. Then initially, both the player doesn't have the ball. But, then one gets the ball
    with ball_toggle, and handsoff to the other player. The test assumes dice rolls results
    differently.
    '''
    def test_handoff_function(self):
        '''
        testing handoff function
        '''
        # instantiate two players
        player1 = game_piece(6, 13, 'running back')
        player2 = game_piece(20, 1, 'lineman 1')

        # both player shouldn't have ball by default
        self.assertEqual(0, player1.has_ball)
        self.assertEqual(0, player2.has_ball)

        # suppose player 1 has the ball, but player 2 doesn't
        player1.ball_toggle()
        self.assertEqual(1, player1.has_ball)

        # now, handoff the ball from player1 to player2
        handoff(player1, player2)

        # now, player2 should have the ball, player1 shouldn't
        # assuming the dices are rolled with different numbers
        self.assertEqual(0, player1.has_ball)
        self.assertEqual(1, player2.has_ball)

    def test_handoff_function2(self):
        '''
        testing handoff function
        '''
        # instantiate two players
        player1 = game_piece(6, 13, 'running back')
        player2 = game_piece(20, 1, 'lineman 1')

        # both player shouldn't have ball by default
        self.assertEqual(0, player1.has_ball)
        self.assertEqual(0, player2.has_ball)

        # suppose player 1 has the ball, but player 2 doesn't
        player2.ball_toggle()
        self.assertEqual(1, player2.has_ball)

        # now, handoff the ball from player1 to player2
        handoff(player1, player2)

        # now, player2 should have the ball, player1 shouldn't
        # assuming the dices are rolled with different numbers
        self.assertEqual(1, player1.has_ball)
        self.assertEqual(0, player2.has_ball)