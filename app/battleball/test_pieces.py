'''
This file tests the pieces object
'''
import unittest
from mock import patch
from app.battleball.game_cli.game_pieces import game_piece, instatiate_pieces, \
                                                check_movement, touchdown, check_move, \
                                                calculate_move

from app.battleball.game_cli.battle_board import create_gameboard, check_adjacent, move

class TESTGAMEPIECES(unittest.TestCase):
    ''' testing of pieces '''
    def test_has_ball_initialized(self):
        ''' test ball_toggle '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.has_ball)

    def test_not_injured_initialized(self):
        ''' test injury '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.injured)

    def test_game_piece_ball_toggle(self):
        ''' test ball toggle on game piece '''
        piece = game_piece(20, 1, 'name')
        piece.ball_toggle()
        self.assertEqual(1, piece.has_ball)

    def test_x_position_initialized(self):
        ''' test game_piece x position '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(-1, piece.position['xpos'])

    def test_y_position_initialized(self):
        ''' test game piece y position '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(-1, piece.position['ypos'])

    def test_y_p2_psize2_initialize(self):
        ''' test heavy tackle y2 position '''
        piece = game_piece(20, 2, 'name')
        self.assertEqual(-2, piece.position['ypos2'])

    def test_roll_size_initialized(self):
        ''' test roll size '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(20, piece.roll_size)

    def test_psize_initialized(self):
        ''' test piece size '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(1, piece.psize)

    def test_place_on_board(self):
        ''' test placement of piece on board '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        self.assertEqual(3, piece.position['xpos'])
        self.assertEqual(2, piece.position['ypos'])

    def test_place_psize2_on_board(self):
        ''' test placement of size 2 piece on board '''
        piece = game_piece(20, 2, 'name')
        piece.place_on_board(3, 2)
        self.assertEqual(3, piece.position['xpos'])
        self.assertEqual(2, piece.position['ypos'])
        self.assertEqual(3, piece.position['ypos2'])

    def test_gp_movement(self):
        ''' test movement of piece '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(5, 2)
        piece.move(1, 2)
        self.assertEqual(6, piece.position['xpos'])
        self.assertEqual(4, piece.position['ypos'])

    def test_psize2_movement(self):
        ''' test movement of size 2 piece '''
        piece = game_piece(20, 2, 'name')
        piece.place_on_board(5, 2)
        piece.move(1, 2)
        self.assertEqual(6, piece.position['xpos'])
        self.assertEqual(4, piece.position['ypos'])
        self.assertEqual(5, piece.position['ypos2'])

    def test_low_injury(self):
        ''' test mild injury '''
        piece = game_piece(20, 1, 'name')
        piece.injury(1)
        self.assertEqual(1, piece.injured)

    def test_high_injury(self):
        ''' test severe injury '''
        piece = game_piece(20, 1, 'name')
        piece.injury(2)
        self.assertEqual(2, piece.injured)

@patch('random.randint', return_value=3)
class TestDice(unittest.TestCase):
    ''' tests rolls of dice '''
    def test_six_sided_dice(self, mocked_randint):
        ''' test the roll of a 6 sided dice '''
        piece = game_piece(6, 2, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 6)
        self.assertEqual(result, 3)

    def test_eight_sided_dice(self, mocked_randint):
        ''' test the roll of an 8 sided dice '''
        piece = game_piece(8, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 8)
        self.assertEqual(result, 3)

    def test_ten_sided_dice(self, mocked_randint):
        ''' test the roll of a 10 sided dice '''
        piece = game_piece(10, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 10)
        self.assertEqual(result, 3)

    def test_twelve_sided_dice(self, mocked_randint):
        ''' test the roll of a 12 sided dice '''
        piece = game_piece(12, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 12)
        self.assertEqual(result, 3)

    def test_twenty_sided_dice(self, mocked_randint):
        ''' test the roll of a 20 sided dice '''
        piece = game_piece(20, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 20)
        self.assertEqual(result, 3)

class TestCreate(unittest.TestCase):
    ''' test creation functions '''

    def test_lineman1_home(self):
        ''' test creation of first lineman, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][2].name, 'lineman 1')

    def test_lineman2_home(self):
        ''' test creation of second lineman, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][3].name, 'lineman 2')

    def test_linebacker1_home(self):
        ''' test creation of linebacker 1, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][4].name, 'linebacker 1')

    def test_linebacker2_home(self):
        ''' test creation of linebacker 2, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][5].name, 'linebacker 2')

    def test_safety1_home(self):
        ''' test creation of safety 1, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][6].name, 'safety 1')

    def test_safety2_home(self):
        ''' test creation of safety 2, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][7].name, 'safety 2')

    def test_runningback1_home(self):
        ''' test creation of running back 1, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][8].name, 'running back 1')

    def test_runningback2_home(self):
        ''' test creation of running back 2, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][9].name, 'running back 2')

    def test_runningback3_home(self):
        ''' test creation of running back 3, home '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][10].name, 'running back 3')

    def test_heavy_tackle_away(self):
        ''' test creation of heavy tackle, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][0].name, 'heavy tackle')

    def test_tackle_away(self):
        ''' test creation of tackle, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][1].name, 'tackle')

    def test_lineman1_away(self):
        ''' test creation of lineman 1, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][2].name, 'lineman 1')

    def test_lineman2_away(self):
        ''' test creation of lineman 2, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][3].name, 'lineman 2')

    def test_linebacker1_away(self):
        ''' test creation of linebacker 1, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][4].name, 'linebacker 1')

    def test_linebacker2_away(self):
        ''' test creation of linebacker 2, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][5].name, 'linebacker 2')

    def test_safety1_away(self):
        ''' test creation of safety 1, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][6].name, 'safety 1')

    def test_safety2_away(self):
        ''' test creation of safety 2, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][7].name, 'safety 2')

    def test_runningback1_away(self):
        ''' test creation of running back 1, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][8].name, 'running back 1')

    def test_runningback2_away(self):
        ''' test creation of running back 2, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][9].name, 'running back 2')

    def test_runningback3_away(self):
        ''' test creation of running back 3, away '''
        players = instatiate_pieces()
        self.assertEqual(players['away'][10].name, 'running back 3')

class TestCheckMovement(unittest.TestCase):
    ''' test piece movements '''
    def test_correct_length_home(self):
        ''' test number of home pieces '''
        players = instatiate_pieces()
        self.assertEqual(len(players['home']), 11)

    def test_correct_length_away(self):
        ''' test number of away pieces '''
        players = instatiate_pieces()
        self.assertEqual(len(players['away']), 11)

    def test_heavy_tackle_home(self):
        ''' test creation of heavy tackle, home team '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][0].name, 'heavy tackle')

    def test_tackle_home(self):
        ''' test creation of tackle, home team '''
        players = instatiate_pieces()
        self.assertEqual(players['home'][1].name, 'tackle')

    def test_legal_movement(self):
        ''' proper movement '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(1, 1)
        roll_value = 10
        to_position = (2, 3)
        check = check_movement(piece, roll_value, to_position)
        self.assertEqual(check, True)

    def test_illegal_movement(self):
        ''' test improper movement '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(1, 1)
        roll_value = 1
        to_position = (2, 3)
        check = check_movement(piece, roll_value, to_position)
        self.assertEqual(check, False)

    def test_return_expected_odd(self):
        ''' test adjacent function '''
        gameboard = create_gameboard()
        gameboard[2][1] = 'B'
        gameboard[2][2] = 'X'
        gameboard[3][1] = 'E'
        gameboard[3][3] = 2
        gameboard[4][1] = 10
        gameboard[4][2] = 8
        adjacent = check_adjacent(gameboard, 3, 2)
        self.assertEqual(adjacent['ul'], 'B')
        self.assertEqual(adjacent['ur'], 'X')
        self.assertEqual(adjacent['l'], 'E')
        self.assertEqual(adjacent['r'], 2)
        self.assertEqual(adjacent['dl'], 10)
        self.assertEqual(adjacent['dr'], 8)

    def test_return_expected_even(self):
        ''' test adjacent function '''
        gameboard = create_gameboard()
        gameboard[1][2] = 'B'
        gameboard[1][3] = 'X'
        gameboard[2][1] = 'E'
        gameboard[2][3] = 2
        gameboard[3][2] = 10
        gameboard[3][3] = 8
        adjacent = check_adjacent(gameboard, 2, 2)
        self.assertEqual(adjacent['ul'], 'B')
        self.assertEqual(adjacent['ur'], 'X')
        self.assertEqual(adjacent['l'], 'E')
        self.assertEqual(adjacent['r'], 2)
        self.assertEqual(adjacent['dl'], 10)
        self.assertEqual(adjacent['dr'], 8)

    def test_board_move_ht(self):
        ''' test adjacent function on heavy tackle '''
        gameboard = create_gameboard()
        gameboard[10][1] = 0
        gameboard[10][2] = 0
        move(gameboard, 0, 10, 1, 11, 1)
        self.assertEqual(gameboard[10][1], 'E')
        self.assertEqual(gameboard[10][2], 'E')
        self.assertEqual(gameboard[11][1], 0)
        self.assertEqual(gameboard[11][2], 0)

    def test_board_move_other(self):
        ''' test move '''
        gameboard = create_gameboard()
        gameboard[10][3] = 8
        move(gameboard, 8, 10, 3, 11, 3)
        self.assertEqual(gameboard[10][3], 'E')
        self.assertEqual(gameboard[10][4], 'E')
        self.assertEqual(gameboard[11][3], 8)
        self.assertEqual(gameboard[11][4], 'E')

class TestTouchdown(unittest.TestCase):
    ''' test touchdown functions '''
    def test_home_touchdown_row_31(self):
        ''' test touchdown at row 31 '''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'home'
        to_location = (31, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_home_touchdown_row_32(self):
        ''' test touchdown at row 32 '''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'home'
        to_location = (32, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_home_not_touchdown_row_31(self):
        ''' test (not a) touchdown at row 31 '''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'home'
        to_location = (31, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

    def test_away_touchdown_row_01(self):
        ''' test away team touchdown at row 1'''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'away'
        to_location = (1, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_away_touchdown_row_00(self):
        ''' test away team touchdown at row 0 '''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'away'
        to_location = (0, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_away_not_touchdown_row_01(self):
        ''' test away team (not a) touchdown at row 1 '''
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'away'
        to_location = (1, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

class TestCheckMove(unittest.TestCase):
    ''' test move '''
    def test_legal_move_ht(self):
        ''' test move legality '''
        piece = game_piece(20, 2, 'heavy tackle')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = 'E'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_illegal_move_ht(self):
        ''' test move legality '''
        piece = game_piece(20, 2, 'heavy tackle')
        location = (2, 15)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = 'E'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_heavy_tackle_offcolumn(self):
        ''' test moving heavy tackle '''
        piece = game_piece(20, 2, 'heavy tackle')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = 'E'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_other_off_column(self):
        ''' test moving non heavy tackle '''
        piece = game_piece(20, 1, 'name')
        location = (1, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_move_piece_off_top(self):
        ''' test move piece off top '''
        piece = game_piece(20, 1, 'name')
        location = (-1, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, False)

    def test_move_piece_off_bottom(self):
        ''' test move piece off bottom '''
        piece = game_piece(20, 1, 'name')
        location = (3, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_piece_on_another_piece(self):
        ''' test moving piece on another '''
        piece = game_piece(20, 1, 'name')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = '1'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, False)


class TestCalculateMove(unittest.TestCase):
    ''' test move '''
    def test_even_ul(self):
        ''' test ul move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'ul')
        self.assertEqual(new_move['row'], 1)
        self.assertEqual(new_move['col'], 2)

    def test_even_ur(self):
        ''' test ur move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'ur')
        self.assertEqual(new_move['row'], 1)
        self.assertEqual(new_move['col'], 3)

    def test_even_l(self):
        ''' test l move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'l')
        self.assertEqual(new_move['row'], 2)
        self.assertEqual(new_move['col'], 1)

    def test_even_r(self):
        ''' test r move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'r')
        self.assertEqual(new_move['row'], 2)
        self.assertEqual(new_move['col'], 3)

    def test_even_dl(self):
        ''' test dl move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'dl')
        self.assertEqual(new_move['row'], 3)
        self.assertEqual(new_move['col'], 2)

    def test_even_dr(self):
        ''' test dr move for piece in even row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(2, 2)
        new_move = calculate_move(piece, 'dr')
        self.assertEqual(new_move['row'], 3)
        self.assertEqual(new_move['col'], 3)

    def test_odd_ul(self):
        ''' test ul move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'ul')
        self.assertEqual(new_move['row'], 2)
        self.assertEqual(new_move['col'], 1)

    def test_odd_ur(self):
        ''' test ur move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'ur')
        self.assertEqual(new_move['row'], 2)
        self.assertEqual(new_move['col'], 2)

    def test_odd_l(self):
        ''' test l move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'l')
        self.assertEqual(new_move['row'], 3)
        self.assertEqual(new_move['col'], 1)

    def test_odd_r(self):
        ''' test r move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'r')
        self.assertEqual(new_move['row'], 3)
        self.assertEqual(new_move['col'], 3)

    def test_odd_dl(self):
        ''' test dl move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'dl')
        self.assertEqual(new_move['row'], 4)
        self.assertEqual(new_move['col'], 1)

    def test_odd_dr(self):
        ''' test dr move for piece in odd row '''
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        new_move = calculate_move(piece, 'dr')
        self.assertEqual(new_move['row'], 4)
        self.assertEqual(new_move['col'], 2)
