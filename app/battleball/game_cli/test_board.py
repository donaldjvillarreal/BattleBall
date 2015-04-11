import unittest
import battle_board as br

class BoardTest(unittest.TestCase):

    def test_board_size(self):
        self.assertEqual(len(br.create_gameboard()),33)

    def test_length_of_endzone1(self):
        self.assertEqual(len(br.create_gameboard()[0]),16)

    def test_length_of_row1(self):
        self.assertEqual(len(br.create_gameboard()[1]),16)

    def test_length_of_row2(self):
        self.assertEqual(len(br.create_gameboard()[2]),15)

    def test_length_of_row3(self):
        self.assertEqual(len(br.create_gameboard()[3]),16)

    def test_length_of_row4(self):
        self.assertEqual(len(br.create_gameboard()[4]),15)

    def test_length_of_row5(self):
        self.assertEqual(len(br.create_gameboard()[5]),16)

    def test_length_of_row6(self):
        self.assertEqual(len(br.create_gameboard()[6]),15)

    def test_length_of_row7(self):
        self.assertEqual(len(br.create_gameboard()[7]),16)

    def test_length_of_row8(self):
        self.assertEqual(len(br.create_gameboard()[8]),15)

    def test_length_of_row9(self):
        self.assertEqual(len(br.create_gameboard()[9]),16)

    def test_length_of_row10(self):
        self.assertEqual(len(br.create_gameboard()[10]),15)

    def test_length_of_row11(self):
        self.assertEqual(len(br.create_gameboard()[11]),16)

    def test_length_of_row12(self):
        self.assertEqual(len(br.create_gameboard()[12]),15)

    def test_length_of_row13(self):
        self.assertEqual(len(br.create_gameboard()[13]),16)

    def test_length_of_row14(self):
        self.assertEqual(len(br.create_gameboard()[14]),15)

    def test_length_of_row15(self):
        self.assertEqual(len(br.create_gameboard()[15]),16)

    def test_length_of_row16(self):
        self.assertEqual(len(br.create_gameboard()[16]),15)

    def test_for_ball(self):
        self.assertEqual(br.create_gameboard()[16][7],'B')

    def test_length_of_row17(self):
        self.assertEqual(len(br.create_gameboard()[17]),16)

    def test_length_of_row18(self):
        self.assertEqual(len(br.create_gameboard()[18]),15)

    def test_length_of_row19(self):
        self.assertEqual(len(br.create_gameboard()[19]),16)

    def test_length_of_row20(self):
        self.assertEqual(len(br.create_gameboard()[20]),15)

    def test_length_of_row21(self):
        self.assertEqual(len(br.create_gameboard()[21]),16)

    def test_length_of_row22(self):
        self.assertEqual(len(br.create_gameboard()[22]),15)

    def test_length_of_row23(self):
        self.assertEqual(len(br.create_gameboard()[23]),16)

    def test_length_of_row24(self):
        self.assertEqual(len(br.create_gameboard()[24]),15)

    def test_length_of_row25(self):
        self.assertEqual(len(br.create_gameboard()[25]),16)

    def test_length_of_row26(self):
        self.assertEqual(len(br.create_gameboard()[26]),15)

    def test_length_of_row27(self):
        self.assertEqual(len(br.create_gameboard()[27]),16)

    def test_length_of_row28(self):
        self.assertEqual(len(br.create_gameboard()[28]),15)

    def test_length_of_row29(self):
        self.assertEqual(len(br.create_gameboard()[29]),16)

    def test_length_of_row30(self):
        self.assertEqual(len(br.create_gameboard()[30]),15)

    def test_length_of_row31(self):
        self.assertEqual(len(br.create_gameboard()[31]),16)

    def test_length_of_endzone2(self):
        self.assertEqual(len(br.create_gameboard()[32]),16)

class TestPlacePiece(unittest.TestCase):
    
    def test_place_piece(self):
        board = br.create_gameboard()
        location = (0,0)
        br.place_piece('0', location,board)
        self.assertEqual(board[0][0],'0')

    def test_place_piece_on_piece(self):
        board = br.create_gameboard()
        location = (1,1)
        br.place_piece('0',location,board)
        self.assertEqual(br.place_piece('2', location, board),False)

class TestResolveFumble(unittest.TestCase):

    def test_place_piece(self):
        board = br.create_gameboard()
        location = (1,1)
        br.resolve_fumble(location,board)
        self.assertEqual(board[1][1],'B')

class TestEmptySpace(unittest.TestCase):

    def test_empty_space(self):
        board = br.create_gameboard()
        x = 16
        y = 7
        self.assertEqual(br.empty_space(board, x, y), True)

    def test_full_space(self):
        board = br.create_gameboard()
        x = 16
        y = 7
        board[x][y] = '0'
        self.assertEqual(br.empty_space(board, x, y), False)