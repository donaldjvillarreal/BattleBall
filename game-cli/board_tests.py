import unittest
import create_board as br

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