'''
This is the unittest code for the tackle function which
is implemented in 'tackel.py'. This function takes two inputs
as game piece objects. The function should rolls their dice
and compares which one is smaller. The smaller one is considered
injured and it's out of the game. The losing piece is returned to
the function that calls it.
'''

import unittest
from battleball.game_cli.tackle import tackle
from battleball.game_cli.game_pieces import game_piece

class TESTTACKLE(unittest.TestCase):
    '''
    Two instances of game piece (player) are created.
    Each with different roll size (dice) and position.
    '''
    def test_tackle_function(self):
        '''
        Then initially, both the players aren't injured.
        But, after the two players tackle, one gets injured
        (outta game) and other is not (keep playing).
        '''
        # instantiate two game piece objects
        player1 = game_piece(20, 5, 'lineman')
        player2 = game_piece(8, 17, 'running back')

        # make sure both the players are not injured initially
        self.assertEqual(0, player1.injured)
        self.assertEqual(0, player2.injured)

        # now let the two players tackle by calling tackle function
        # return player is one who lose the tackle
        playerinjured = tackle(player1, player2)

        # now set the returned player's injured attribute as True
        playerinjured.injured = 1

        # make sure the player who lost tackle is injured and other is not
        if playerinjured == player1:
            self.assertEqual(1, player1.injured)
            self.assertEqual(0, player2.injured)
        else:
            self.assertEqual(1, player2.injured)
            self.assertEqual(0, player1.injured)


