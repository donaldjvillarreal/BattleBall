'''
This is the unittest code for the tackle function which
is implemented in 'tackel.py'. This function takes two inputs 
as game piece objects. The function should rolls their dice
and compares which one is smaller. The smaller one is considered
injured and it's out of the game. The losing piece is returned to 
the function that calls it.
'''

import unittest
from tackle import tackle
from game_pieces import game_piece


