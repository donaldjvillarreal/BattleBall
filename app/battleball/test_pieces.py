'''
This file tests the pieces object
'''
import unittest
from mock import Mock, patch
from battleball.game_cli.game_pieces import game_piece, instatiate_pieces, check_movement, touchdown, check_move
from battleball.game_cli.battle_board import create_gameboard, check_adjacent, move

class test_pieces(unittest.TestCase):

    def test_game_piece_has_ball_initialized(self):
        ''' test ball_toggle '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.has_ball)

    def test_game_piece_not_injured_initialized(self):
        ''' test injury '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.injured)

    def test_game_piece_ball_toggle(self):
        ''' test ball toggle on game piece '''
        piece = game_piece(20, 1, 'name')
        piece.ball_toggle()
        self.assertEqual(1, piece.has_ball)

    def test_game_piece_x_position_initialized(self):
        ''' test game_piece x position '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(-1, piece.position['xpos'])

    def test_game_piece_y_position_initialized(self):
        ''' test game piece y position '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(-1, piece.position['ypos'])

    def test_game_piece_y_position2_psize2_initialize(self):
        ''' test heavy tackle y2 position '''
        piece = game_piece(20, 2, 'name')
        self.assertEqual(-2, piece.position['ypos2'])

    def test_game_piece_roll_size_initialized(self):
        ''' test roll size '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(20, piece.roll_size)

    def test_game_piece_psize_initialized(self):
        ''' test piece size '''
        piece = game_piece(20, 1, 'name')
        self.assertEqual(1, piece.psize)

    def test_game_piece_place_on_board(self):
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(3, 2)
        self.assertEqual(3, piece.position['xpos'])
        self.assertEqual(2, piece.position['ypos'])

    def test_game_piece_place_psize2_on_board(self):
        piece = game_piece(20, 2, 'name')
        piece.place_on_board(3, 2)
        self.assertEqual(3, piece.position['xpos'])
        self.assertEqual(2, piece.position['ypos'])
        self.assertEqual(3, piece.position['ypos2'])

    def test_game_piece_movement(self):
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(5, 2)
        piece.move(1, 2)
        self.assertEqual(6, piece.position['xpos'])
        self.assertEqual(4, piece.position['ypos'])

    def test_game_piece_psize2_movement(self):
        piece = game_piece(20, 2, 'name')
        piece.place_on_board(5, 2)
        piece.move(1, 2)
        self.assertEqual(6, piece.position['xpos'])
        self.assertEqual(4, piece.position['ypos'])
        self.assertEqual(5, piece.position['ypos2'])

    def test_game_piece_low_injury(self):
        piece = game_piece(20, 1, 'name')
        piece.injury(1)
        self.assertEqual(1, piece.injured)

    def test_game_piece_high_injury(self):
        piece = game_piece(20, 1, 'name')
        piece.injury(2)
        self.assertEqual(2, piece.injured)

@patch('random.randint', return_value=3)
class TestDice(unittest.TestCase):
    def test_six_sided_dice(self, mocked_randint):
        piece = game_piece(6, 2, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 6)
        self.assertEqual(result, 3)

    def test_eight_sided_dice(self, mocked_randint):
        piece = game_piece(8, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 8)
        self.assertEqual(result, 3)

    def test_ten_sided_dice(self, mocked_randint):
        piece = game_piece(10, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 10)
        self.assertEqual(result, 3)

    def test_twelve_sided_dice(self, mocked_randint):
        piece = game_piece(12, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 12)
        self.assertEqual(result, 3)

    def test_twenty_sided_dice(self, mocked_randint):
        piece = game_piece(20, 1, 'name')
        result = piece.roll()
        mocked_randint.assert_called_with(1, 20)
        self.assertEqual(result, 3)

class TestCreate(unittest.TestCase):
    def test_correct_length_home(self):
        players = instatiate_pieces()
        self.assertEqual(len(players['home']), 11)

    def test_correct_length_away(self):
        players = instatiate_pieces()
        self.assertEqual(len(players['away']), 11)

    def test_heavy_tackle_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][0].name, 'heavy tackle')

    def test_tackle_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][1].name, 'tackle')

    def test_lineman1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][2].name, 'lineman 1')

    def test_lineman2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][3].name, 'lineman 2')

    def test_linebacker1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][4].name, 'linebacker 1')

    def test_linebacker2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][5].name, 'linebacker 2')

    def test_safety1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][6].name, 'safety 1')

    def test_safety2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][7].name, 'safety 2')

    def test_runningback1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][8].name, 'running back 1')

    def test_runningback2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][9].name, 'running back 2')

    def test_runningback3_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][10].name, 'running back 3')

    def test_heavy_tackle_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][0].name, 'heavy tackle')

    def test_tackle_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][1].name, 'tackle')

    def test_lineman1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][2].name, 'lineman 1')

    def test_lineman2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][3].name, 'lineman 2')

    def test_linebacker1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][4].name, 'linebacker 1')

    def test_linebacker2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][5].name, 'linebacker 2')

    def test_safety1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][6].name, 'safety 1')

    def test_safety2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][7].name, 'safety 2')

    def test_runningback1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][8].name, 'running back 1')

    def test_runningback2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][9].name, 'running back 2')

    def test_runningback3_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][10].name, 'running back 3')

class TestCheckMovement(unittest.TestCase):

    def test_legal_movement(self):
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(1, 1)
        roll_value = 10
        to_position = (2, 3)
        check = check_movement(piece, roll_value, to_position)
        self.assertEqual(check, True)

    def test_illegal_movement(self):
        piece = game_piece(20, 1, 'name')
        piece.place_on_board(1, 1)
        roll_value = 1
        to_position = (2, 3)
        check = check_movement(piece, roll_value, to_position)
        self.assertEqual(check, False)

    def test_return_as_expected(self):
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

    def test_board_move_ht(self):
        gameboard = create_gameboard()
        gameboard[10][1] = 0
        gameboard[10][2] = 0
        move(gameboard, 0, 10, 1, 11, 1)
        self.assertEqual(gameboard[10][1], 'E')
        self.assertEqual(gameboard[10][2], 'E')
        self.assertEqual(gameboard[11][1], 0)
        self.assertEqual(gameboard[11][2], 0)

    def test_board_move_other(self):
        gameboard = create_gameboard()
        gameboard[10][3] = 8
        move(gameboard, 8, 10, 3, 11, 3)
        self.assertEqual(gameboard[10][3], 'E')
        self.assertEqual(gameboard[10][4], 'E')
        self.assertEqual(gameboard[11][3], 8)
        self.assertEqual(gameboard[11][4], 'E')

class TestTouchdown(unittest.TestCase):

    def test_home_touchdown_row_31(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'home'
        to_location = (31, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_home_touchdown_row_32(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'home'
        to_location = (32, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_home_not_touchdown_row_31(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'home'
        to_location = (31, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

    def test_home_touchdown_row_32(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'home'
        to_location = (32, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

    def test_away_touchdown_row_01(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'away'
        to_location = (1, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_away_touchdown_row_00(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = True
        team = 'away'
        to_location = (0, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, True)

    def test_away_not_touchdown_row_01(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'away'
        to_location = (1, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

    def test_away_touchdown_row_00(self):
        piece = game_piece(20, 1, 'name')
        piece.has_ball = False
        team = 'away'
        to_location = (0, 7)
        scored = touchdown(piece, to_location, team)
        self.assertEqual(scored, False)

class TestCheckMove(unittest.TestCase):

    def test_legal_move(self):
        piece = game_piece(20, 2, 'heavy tackle')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = 'E'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_move_heavy_tackle_off_column(self):
        piece = game_piece(20, 2, 'heavy tackle')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = 'E'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_move_other_piece_off_column(self):
        piece = game_piece(20, 1, 'name')
        location = (1, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_move_piece_off_top(self):
        piece = game_piece(20, 1, 'name')
        location = (-1, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, False)

    def test_move_piece_off_bottom(self):
        piece = game_piece(20, 1, 'name')
        location = (3, 4)
        gameboard = create_gameboard()
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, True)

    def test_move_piece_on_another_piece(self):
        piece = game_piece(20, 1, 'name')
        location = (1, 4)
        gameboard = create_gameboard()
        gameboard[location[0]][location[1]] = '1'
        check = check_move(piece, location, gameboard)
        self.assertEqual(check, False)
