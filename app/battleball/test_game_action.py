'''
This file ensures the correct JSON file has been created
'''
import unittest
import battleball.game_cli.battle_board as bb
import battleball.game_cli.game_pieces as gp
import battleball.game_cli.game_actions as ga
import json

class Gametest(unittest.TestCase):
    ''' Tests for JSON File '''
    def setUp(self):
        ''' Test Setup '''
        self.board = bb.create_gameboard
        self.home_piece = gp.create_piece
        self.away_piece = gp.create_piece

    def test_board(self):
        ''' test json board '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['board'], self.board)

    def test_home(self):
        ''' test home team dictionary '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['home'], self.home_piece)

    def test_away(self):
        ''' test away team dictionary '''
        filename = ga.create_game_file(1)
        with open(filename) as wfile:
            test = json.load(wfile)
        self.assertEqual(test['game']['away'], self.away_piece)
