import unittest
import battle_board as bb
import game_pieces as gp
import game_actions as ga
import json

class Gametest(unittest.TestCase):

    def setUp(self):
        self.board = bb.create_gameboard
        self.home_piece = gp.create_piece
        self.away_piece = gp.create_piece

    def test_board(self):
        filename = ga.create_game_file(1)
        with open(filename) as f:
            test = json.load(f)
        self.assertEqual(test['game']['board'], self.board)

    def test_home(self):
        filename = ga.create_game_file(1)
        with open(filename) as f:
            test = json.load(f)
        self.assertEqual(test['game']['home'], self.home_piece)

    def test_away(self):
        filename = ga.create_game_file(1)
        with open(filename) as f:
            test = json.load(f)
        self.assertEqual(test['game']['away'], self.away_piece)