import unittest
from game_pieces import game_piece

class test_pieces(unittest.TestCase):
    def test_game_piece_has_ball_initialized(self):
        piece = game_piece()
        self.assertEqual(0, piece.has_ball)

    def test_game_piece_not_injured_initialized(self):
        piece = game_piece()
        self.assertEqual(0, piece.injured)

    def test_game_piece_ball_toggle(self):
        piece = game_piece()
        piece.ball_toggle()
        self.assertEqual(1, piece.has_ball)

    def test_x_position_initialized(self):
    	piece = game_piece()
    	self.assertEqual(-1, piece.position['xpos1'])

    def test_y_position_initialized(self):
    	piece = game_piece()
    	self.assertEqual(-1, piece.position['ypos1'])

    def test_place_on_board(self):
    	piece = game_piece()
    	piece.place_on_board(3,2)
    	self.assertEqual(3, piece.position['xpos1'])
    	self.assertEqual(2, piece.position['ypos1'])

    def test_movement(self):
    	piece = game_piece()
    	piece.place_on_board(5,2)
    	piece.move(1,2)
    	self.assertEqual(6, piece.position['xpos1'])
    	self.assertEqual(4, piece.position['ypos1'])


if __name__ == '__main__':
    unittest.main()
