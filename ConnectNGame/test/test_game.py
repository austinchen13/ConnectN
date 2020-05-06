import unittest
from unittest.mock import patch
from ConnectNGame.test.print_capturer import PrintCapturer
from ConnectNGame.src.game import Game


class TestGame(unittest.TestCase):
    def test_make_two_players(self):
        user_input = ["Austin", "P", "Bob", "X"]
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            a = Game(3, 3, 3, "O")
            a.make_two_players()
            self.assertEqual(a.player1.name, "Austin")
            self.assertEqual(a.player2.name, "Bob")
            self.assertEqual(a.player1.piece, "P")
            self.assertEqual(a.player2.piece, "X")

    def test_wrong_input_for_make_two_players(self):
        user_input = ["   ", "Kobe", "dog", "Kobe", "X", "Juice", "X", "Juice", "L"]
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            a = Game(3, 3, 3, "O")
            a.make_two_players()
            self.assertEqual(a.player1.name, "Kobe")
            self.assertEqual(a.player2.name, "Juice")
            self.assertEqual(a.player1.piece, "X")
            self.assertEqual(a.player2.piece, "L")

    def test_initialize_game(self):
        capture = PrintCapturer()
        with patch('ConnectNGame.src.game.print', side_effect=capture):
            a = Game(3, 3, 3, "x")
            a.initialize_game()
            board_output = "  0 1 2\n" \
                           "0 x x x\n" \
                           "1 x x x\n" \
                           "2 x x x\n"
            self.assertEqual(board_output, capture.as_string())

    def test_place_piece(self):
        capture = PrintCapturer()
        with patch('ConnectNGame.src.game.print', side_effect=capture):
            a = Game(3, 3, 3, "x")
            a.initialize_game()
            a._place_piece(2, "P")
            a._place_piece(2, "P")
            board_output = "  0 1 2\n" \
                           "0 x x x\n" \
                           "1 x x x\n" \
                           "2 x x x\n" \
                           "  0 1 2\n" \
                           "0 x x x\n" \
                           "1 x x x\n" \
                           "2 x x P\n" \
                           "  0 1 2\n" \
                           "0 x x x\n" \
                           "1 x x P\n" \
                           "2 x x P\n"

            self.assertEqual(board_output, capture.as_string())

    def test_check_for_win_horizontal(self):
        a = Game(3, 3, 3, "x")
        a.initialize_game()
        a._place_piece(2, "P")
        a._place_piece(1, "P")
        a._place_piece(0, "P")
        self.assertEqual(a._check_for_win("P"), True)

    def test_check_for_win_vertical(self):
        a = Game(4, 4, 4, "x")
        a.initialize_game()
        a._place_piece(3, "P")
        a._place_piece(2, "P")
        a._place_piece(1, "P")
        a._place_piece(0, "P")
        self.assertEqual(a._check_for_win("P"), True)

    def test_check_for_win_right_diagonal(self):
        a = Game(3, 3, 3, "x")
        a.initialize_game()
        a._place_piece(2, "O")
        a._place_piece(1, "X")
        a._place_piece(1, "O")
        a._place_piece(0, "X")
        a._place_piece(0, "O")
        a._place_piece(1, "X")
        a._place_piece(0, "O")
        self.assertEqual(a._check_for_win("O"), True)

    def test_check_for_win_left_diagonal(self):
        a = Game(3, 3, 3, "x")
        a.initialize_game()
        a._place_piece(0, "O")
        a._place_piece(1, "X")
        a._place_piece(1, "O")
        a._place_piece(2, "X")
        a._place_piece(2, "O")
        a._place_piece(1, "X")
        a._place_piece(2, "O")
        self.assertEqual(a._check_for_win("O"), True)








if __name__ == '__main__':
    unittest.main()
