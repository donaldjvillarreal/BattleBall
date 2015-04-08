import unittest
from mock import Mock, patch
from game_pieces import game_piece, instatiate_pieces

class test_pieces(unittest.TestCase):

    def test_game_piece_has_ball_initialized(self):
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.has_ball)

    def test_game_piece_not_injured_initialized(self):
        piece = game_piece(20, 1, 'name')
        self.assertEqual(0, piece.injured)

    def test_game_piece_ball_toggle(self):
        piece = game_piece(20, 1, 'name')
        piece.ball_toggle()
        self.assertEqual(1, piece.has_ball)

    def test_game_piece_x_position_initialized(self):
    	piece = game_piece(20, 1, 'name')
    	self.assertEqual(-1, piece.position['xpos'])

    def test_game_piece_y_position_initialized(self):
    	piece = game_piece(20, 1, 'name')
    	self.assertEqual(-1, piece.position['ypos'])

    def test_game_piece_y_position2_psize2_initialize(self):
    	piece = game_piece(20, 2, 'name')
    	self.assertEqual(-2, piece.position['ypos2'])

    def test_game_piece_roll_size_initialized(self):
    	piece = game_piece(20, 1, 'name')
    	self.assertEqual(20, piece.roll_size)

    def test_game_piece_psize_initialized(self):
    	piece = game_piece(20, 1, 'name')
    	self.assertEqual(1, piece.psize)

    def test_game_piece_place_on_board(self):
    	piece = game_piece(20, 1, 'name')
    	piece.place_on_board(3,2)
    	self.assertEqual(3, piece.position['xpos'])
    	self.assertEqual(2, piece.position['ypos'])

    def test_game_piece_place_psize2_on_board(self):
    	piece = game_piece(20, 2, 'name')
    	piece.place_on_board(3,2)
    	self.assertEqual(3, piece.position['xpos'])
    	self.assertEqual(2, piece.position['ypos'])
    	self.assertEqual(3, piece.position['ypos2'])

    def test_game_piece_movement(self):
    	piece = game_piece(20, 1, 'name')
    	piece.place_on_board(5,2)
    	piece.move(1,2)
    	self.assertEqual(6, piece.position['xpos'])
    	self.assertEqual(4, piece.position['ypos'])

    def test_game_piece_psize2_movement(self):
    	piece = game_piece(20, 2, 'name')
    	piece.place_on_board(5,2)
    	piece.move(1,2)
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
    	piece = game_piece(6,2, 'name')
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,6)
    	self.assertEqual(result, 3)

    def test_eight_sided_dice(self, mocked_randint):
    	piece = game_piece(8,1, 'name')
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,8)
    	self.assertEqual(result, 3)

    def test_ten_sided_dice(self, mocked_randint):
    	piece = game_piece(10,1, 'name')
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,10)
    	self.assertEqual(result, 3)

    def test_twelve_sided_dice(self, mocked_randint):
    	piece = game_piece(12,1, 'name')
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,12)
    	self.assertEqual(result, 3)

    def test_twenty_sided_dice(self, mocked_randint):
    	piece = game_piece(20,1, 'name')
    	result = piece.roll()
    	mocked_randint.assert_called_with(1,20)
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
        self.assertEqual(players['home'][0].name, 'heavy tackle' )

    def test_tackle_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][1].name, 'tackle' )

    def test_lineman1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][2].name, 'lineman 1' )

    def test_lineman2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][3].name, 'lineman 2' )

    def test_linebacker1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][4].name, 'linebacker 1' )

    def test_linebacker2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][5].name, 'linebacker 2' )

    def test_safety1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][6].name, 'safety 1' )

    def test_safety2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][7].name, 'safety 2' )

    def test_runningback1_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][8].name, 'running back 1' )

    def test_runningback2_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][9].name, 'running back 2' )

    def test_runningback3_home(self):
        players = instatiate_pieces()
        self.assertEqual(players['home'][10].name, 'running back 3' )

    def test_heavy_tackle_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][0].name, 'heavy tackle' )

    def test_tackle_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][1].name, 'tackle' )

    def test_lineman1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][2].name, 'lineman 1' )

    def test_lineman2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][3].name, 'lineman 2' )

    def test_linebacker1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][4].name, 'linebacker 1' )

    def test_linebacker2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][5].name, 'linebacker 2' )

    def test_safety1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][6].name, 'safety 1' )

    def test_safety2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][7].name, 'safety 2' )

    def test_runningback1_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][8].name, 'running back 1' )

    def test_runningback2_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][9].name, 'running back 2' )

    def test_runningback3_away(self):
        players = instatiate_pieces()
        self.assertEqual(players['away'][10].name, 'running back 3' )