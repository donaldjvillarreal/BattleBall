import unittest
from mock import Mock, patch
from game_pieces import game_piece

class test_pieces(unittest.TestCase):

    def test_game_piece_has_ball_initialized(self):
        piece = game_piece(20, 1)
        self.assertEqual(0, piece.has_ball)

    def test_game_piece_not_injured_initialized(self):
        piece = game_piece(20, 1)
        self.assertEqual(0, piece.injured)

    def test_game_piece_ball_toggle(self):
        piece = game_piece(20, 1)
        piece.ball_toggle()
        self.assertEqual(1, piece.has_ball)

    def test_game_piece_x_position_initialized(self):
    	piece = game_piece(20, 1)
    	self.assertEqual(-1, piece.position['xpos'])

    def test_game_piece_y_position_initialized(self):
    	piece = game_piece(20, 1)
    	self.assertEqual(-1, piece.position['ypos'])

    def test_game_piece_y_position2_psize2_initialize(self):
    	piece = game_piece(20, 2)
    	self.assertEqual(-2, piece.position['ypos2'])

    def test_game_piece_roll_size_initialized(self):
    	piece = game_piece(20, 1)
    	self.assertEqual(20, piece.roll_size)

    def test_game_piece_psize_initialized(self):
    	piece = game_piece(20, 1)
    	self.assertEqual(1, piece.psize)

    def test_game_piece_place_on_board(self):
    	piece = game_piece(20, 1)
    	piece.place_on_board(3,2)
    	self.assertEqual(3, piece.position['xpos'])
    	self.assertEqual(2, piece.position['ypos'])

    def test_game_piece_place_psize2_on_board(self):
    	piece = game_piece(20, 2)
    	piece.place_on_board(3,2)
    	self.assertEqual(3, piece.position['xpos'])
    	self.assertEqual(2, piece.position['ypos'])
    	self.assertEqual(3, piece.position['ypos2'])

    def test_game_piece_movement(self):
    	piece = game_piece(20, 1)
    	piece.place_on_board(5,2)
    	piece.move(1,2)
    	self.assertEqual(6, piece.position['xpos'])
    	self.assertEqual(4, piece.position['ypos'])

    def test_game_piece_psize2_movement(self):
    	piece = game_piece(20, 2)
    	piece.place_on_board(5,2)
    	piece.move(1,2)
    	self.assertEqual(6, piece.position['xpos'])
    	self.assertEqual(4, piece.position['ypos'])
    	self.assertEqual(5, piece.position['ypos2'])

    def test_game_piece_low_injury(self):
        piece = game_piece(20, 1)
        piece.injury(1)
        self.assertEqual(1, piece.injured)

    def test_game_piece_high_injury(self):
        piece = game_piece(20, 1)
        piece.injury(2)
        self.assertEqual(2, piece.injured)

@patch('random.randint', return_value=3)
class TestDice(unittest.TestCase):
    def test_six_sided_dice(self, mocked_randint):
    	piece = game_piece(6,2)
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,6)
    	self.assertEqual(result, 3)

    def test_eight_sided_dice(self, mocked_randint):
    	piece = game_piece(8,1)
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,8)
    	self.assertEqual(result, 3)

    def test_ten_sided_dice(self, mocked_randint):
    	piece = game_piece(10,1)
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,10)
    	self.assertEqual(result, 3)

    def test_twelve_sided_dice(self, mocked_randint):
    	piece = game_piece(12,1)
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,12)
    	self.assertEqual(result, 3)

    def test_twenty_sided_dice(self, mocked_randint):
    	piece = game_piece(20,1)
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,20)
    	self.assertEqual(result, 3)

