import unittest
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):
    def test_make_board_list(self):
        a = Board(4, 4, "x")
        list = a.make_board_list()
        self.assertEqual(list, [[" ", "0", "1", "2", "3"], ["0", "x", "x", "x", "x"], ["1", "x", "x", "x", "x"],
                                ["2", "x", "x", "x", "x"], ["3", "x", "x", "x", "x"]])

    def test_repr(self):
        a = Board(3,3, "x")
        a.make_board_list()
        board_output = "  0 1 2\n" \
                       "0 x x x\n" \
                       "1 x x x\n" \
                       "2 x x x"
        self.assertEqual(repr(a), board_output)

    def test_repr_connect_four(self):
        a = Board(6,7, "*")
        a.make_board_list()
        board_output = "  0 1 2 3 4 5 6\n" \
                       "0 * * * * * * *\n" \
                       "1 * * * * * * *\n" \
                       "2 * * * * * * *\n" \
                       "3 * * * * * * *\n" \
                       "4 * * * * * * *\n" \
                       "5 * * * * * * *"
        self.assertEqual(repr(a), board_output)

if __name__ == '__main__':
    unittest.main()
