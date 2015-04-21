'''
This the tackle function:
This function takes as input two game piece objects.
The function should roll the respective pieces die,
compare which one is smaller, update the losing pieces
is_injured attribute and return the losing piece.
'''
from game_pieces import game_piece

def tackle(player1, player2):
    '''
    test if the two players are instances of 'game_pice' class
    if either one of them are not, exception is thrown by 'assert'
    function
    '''
    assert (isinstance(player1, game_piece)) and (isinstance(player2, game_piece))

    # roll the dice for both players
    result1 = player1.roll()
    result2 = player2.roll()

    # it's a do or die sitution, one result
    # should be lower than the other
    # so loop until results unequal
    while result1 == result2:
        result1 = player1.roll()
        result2 = player2.roll()

    # compare which die result is smaller
    if result1 < result2:
        # player1 is injured and out of the game
        player1.injured = 1
        return player1
    else:
        # player2 is injured and out of the game
        player2.injured = 1
        return player2
