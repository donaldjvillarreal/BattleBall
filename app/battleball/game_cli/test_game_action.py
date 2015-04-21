'''
This file ensures the correct JSON file has been created
'''
import unittest
import battle_board as bb
import game_pieces as gp
import game_actions as ga
import json

class Gametest(unittest.TestCase):
    ''' Tests for JSON File '''
    def setUp(self):
        ''' Test Setup '''
        self.board = bb.create_gameboard
        self.home_piece = gp.create_piece
        self.away_piece = gp.create_piece

    def test_board(self):
        ''' Test the board '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['board'], self.board)

    def test_home(self):
        ''' test home team '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['home'], self.home_piece)

    def test_away(self):
        ''' test away team '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['away'], self.away_piece)
