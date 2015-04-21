'''
This file tests for the validity of the board
'''
import unittest
import battle_board as br

class BoardTest(unittest.TestCase):
    ''' Test board creation from command line '''
    def test_board_size(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()), 13)

    def test_length_of_endzone1(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[0]), 6)

    def test_length_of_row1(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[1]), 6)

    def test_length_of_row2(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[2]), 5)

    def test_length_of_row3(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[3]), 6)

    def test_length_of_row4(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[4]), 5)

    def test_length_of_row5(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[5]), 6)

    def test_length_of_row6(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[6]), 5)

    def test_length_of_row7(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[7]), 6)

    def test_length_of_row8(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[8]), 5)

    def test_length_of_row9(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[9]), 6)

    def test_length_of_row10(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[10]), 5)

    def test_length_of_row11(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[11]), 6)

    def test_for_ball(self):
        ''' Test that ball is on board '''
        self.assertEqual(br.create_gameboard()[6][3], 'B')
    '''
    def test_length_of_row12(self):
        self.assertEqual(len(br.create_gameboard()[12]), 15)

    def test_length_of_row13(self):
        self.assertEqual(len(br.create_gameboard()[13]), 16)

    def test_length_of_row14(self):
        self.assertEqual(len(br.create_gameboard()[14]), 15)

    def test_length_of_row15(self):
        self.assertEqual(len(br.create_gameboard()[15]), 16)

    def test_length_of_row16(self):
        self.assertEqual(len(br.create_gameboard()[16]), 15)

    def test_for_ball(self):
        self.assertEqual(br.create_gameboard()[16][7], 'B')

    def test_length_of_row17(self):
        self.assertEqual(len(br.create_gameboard()[17]), 16)

    def test_length_of_row18(self):
        self.assertEqual(len(br.create_gameboard()[18]), 15)

    def test_length_of_row19(self):
        self.assertEqual(len(br.create_gameboard()[19]), 16)

    def test_length_of_row20(self):
        self.assertEqual(len(br.create_gameboard()[20]), 15)

    def test_length_of_row21(self):
        self.assertEqual(len(br.create_gameboard()[21]), 16)

    def test_length_of_row22(self):
        self.assertEqual(len(br.create_gameboard()[22]), 15)

    def test_length_of_row23(self):
        self.assertEqual(len(br.create_gameboard()[23]), 16)

    def test_length_of_row24(self):
        self.assertEqual(len(br.create_gameboard()[24]), 15)

    def test_length_of_row25(self):
        self.assertEqual(len(br.create_gameboard()[25]), 16)

    def test_length_of_row26(self):
        self.assertEqual(len(br.create_gameboard()[26]), 15)

    def test_length_of_row27(self):
        self.assertEqual(len(br.create_gameboard()[27]), 16)

    def test_length_of_row28(self):
        self.assertEqual(len(br.create_gameboard()[28]), 15)

    def test_length_of_row29(self):
        self.assertEqual(len(br.create_gameboard()[29]), 16)

    def test_length_of_row30(self):
        self.assertEqual(len(br.create_gameboard()[30]), 15)

    def test_length_of_row31(self):
        self.assertEqual(len(br.create_gameboard()[31]), 16)
    '''
    def test_length_of_endzone2(self):
        ''' Test individual spots created '''
        self.assertEqual(len(br.create_gameboard()[12]), 6)

class TestPlacePiece(unittest.TestCase):
    '''
    Test placement of piece on board
    '''
    def test_place_piece(self):
        ''' test the placement of a piece '''
        board = br.create_gameboard()
        location = (0, 0)
        br.place_piece('0', location, board)
        self.assertEqual(board[0][0], '0')

    def test_place_piece_on_piece(self):
        ''' test that you cannot place a piece on a piece '''
        board = br.create_gameboard()
        location = (1, 1)
        br.place_piece('0', location, board)
        self.assertEqual(br.place_piece('2', location, board), False)

class TestResolveFumble(unittest.TestCase):
    '''
    Test fumble function
    '''
    def test_place_piece_fumble(self):
        ''' test placement of piece after a fumble '''
        board = br.create_gameboard()
        location = (1, 1)
        br.resolve_fumble(location, board)
        self.assertEqual(board[1][1], 'B')

class TestEmptySpace(unittest.TestCase):
    '''
    Test for empty board
    '''
    def test_empty_space(self):
        ''' test an empty space '''
        board = br.create_gameboard()
        posx = 16
        posy = 7
        self.assertEqual(br.empty_space(board, posx, posy), True)

    def test_full_space(self):
        ''' test a full space '''
        board = br.create_gameboard()
        posx = 16
        posy = 7
        board[posx][posy] = '0'
        self.assertEqual(br.empty_space(board, posx, posy), False)
