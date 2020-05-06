from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player


class Game(object):

    def __init__(self, rows: int, columns: int, pieces_to_win: int, character: str) -> None:
        self.rows = rows
        self.columns = columns
        self.pieces_to_win = pieces_to_win
        self.character = character

    def make_two_players(self) -> None:
        while True:
            p1_name = input("Player 1 enter your name: ")
            p1_name = p1_name.strip()
            if p1_name == "":
                print("Your name cannot be the empty string or whitespace. ")
                continue
            p1_char = input("Player 1 enter your piece: ")
            p1_char = p1_char.strip()
            if p1_char == "":
                print("Your piece cannot be the empty string or whitespace. ")
                continue
            if len(p1_char) > 1:
                print(p1_char + " is not a single character. Your piece can only be a single character. ")
                continue
            if p1_char == self.character:
                print("Your piece cannot be the same as the blank character. ")
                continue
            self.player1 = Player(p1_name, p1_char)
            break
        while True:
            p2_name = input("Player 2 enter your name: ")
            p2_name = p2_name.strip()
            p2_name_lower = p2_name.lower()
            p1_name_lower = p1_name.lower()
            if p2_name == "":
                print("Your name cannot be the empty string or whitespace. ")
                continue
            if p2_name_lower == p1_name_lower:
                print("You cannot use " + p1_name + " for your name as someone else is already using it. ")
                continue
            p2_char = input("Player 2 enter your piece: ")
            p2_char = p2_char.strip()
            p2_char_lower = p2_char.lower()
            p1_char_lower = p1_char.lower()
            if p2_char == "":
                print("Your piece cannot be the empty string or whitespace: ")
                continue
            if len(p2_char) > 1:
                print(p2_char + " is not a single character. Your piece can only be a single character. ")
                continue
            if p2_char == self.character:
                print("Your piece cannot be the same as the blank character. ")
                continue
            if p2_char_lower == p1_char_lower:
                print("You cannot use " + p1_char + " for your piece as " + p1_name + " is already using it. ")
                continue
            self.player2 = Player(p2_name, p2_char)
            break

    def initialize_game(self) -> None:
        self.board = Board(self.rows, self.columns, self.character)
        self.board.make_board_list()
        print(repr(self.board))

    def _place_piece(self, column_choice: int, char: str) -> None:
        i = len(self.board.board_list)
        for row in reversed(self.board.board_list):
            if row[column_choice + 1] == self.character:
                self.board.board_list[i - 1][column_choice + 1] = char
                print(self.board)
                break
            else:
                i = i - 1
                continue

    def _check_for_win(self, char: str) -> bool:
        match = 1
        # horizontal
        for i in range(1, len(self.board.board_list)):
            for j in range(1, self.columns + 1):
                try:
                    if self.board.board_list[i][j] == char and self.board.board_list[i][j + 1] == char:
                        match = match + 1
                        if match == self.pieces_to_win:
                            return True
                        continue
                    else:
                        match = 1
                except:
                    match = 1
        # vertical
        for i in range(1, len(self.board.board_list)):
            for j in range(1, self.columns + 1):
                try:
                    if self.board.board_list[j][i] == char and self.board.board_list[j + 1][i] == char:
                        match = match + 1
                        if match == self.pieces_to_win:
                            return True
                        continue
                    else:
                        match = 1
                except:
                    match = 1
        # left to right diagonal

        for i in range(1, len(self.board.board_list)):
            for j in range(1, self.columns + 1):
                try:
                    while True:
                        if self.board.board_list[i][j] == char and self.board.board_list[i + 1][j + 1] == char:
                            match = match + 1
                            if match == self.pieces_to_win:
                                return True
                            i = i + 1
                            j = j + 1
                            continue
                        else:
                            match = 1
                            break
                except:

                    match = 1
        # right to left diagonal
        for i in range(1, len(self.board.board_list)):
            for j in range(1, self.columns + 1):
                try:
                    while True:
                        if self.board.board_list[i][j] == char and self.board.board_list[i + 1][j - 1] == char:
                            match = match + 1
                            if match == self.pieces_to_win:  # TODO something wrong with check for win
                                return True
                            i = i + 1
                            j = j - 1
                            continue
                        else:
                            match = 1
                            break
                except:

                    match = 1
        return False

    def play(self) -> None:
        while True:
            # Player 1 Turn
            while True:
                print(self.player1.name, end=", ")
                p1_choice = input("please enter the column you want to play in: ")
                try:
                    p1_choice = int(p1_choice)  # type: ignore
                except:
                    print(self.player1.name + ",",
                          "column needs to be an integer. " + p1_choice + " is not an integer.")
                    continue

                if int(p1_choice) > self.columns - 1 or int(p1_choice) < 0:
                    print(
                        "Your column needs to be between 0 and " + str((self.columns - 1)) + " but is actually " + str(
                            p1_choice) + ".")
                    continue

                if self.board.board_list[1][int(p1_choice) + 1] == self.character:
                    break
                else:
                    print("You cannot play in " + str(p1_choice) + " because it is full.")

            self._place_piece(int(p1_choice), self.player1.piece)
            if self._check_for_win(self.player1.piece):
                print(self.player1.name + " won the game!")
                break

            if self.character not in self.board.board_list[1]:
                print("Tie Game.")
                break

            # Player 2 Turn
            while True:
                print(self.player2.name, end=", ")
                p2_choice = input("please enter the column you want to play in: ")
                try:
                    p2_choice = int(p2_choice)  # type: ignore

                except:
                    print(self.player2.name + ",",
                          "column needs to be an integer. " + str(p2_choice )+ " is not an integer.")
                    continue

                if int(p2_choice) > (self.columns - 1) or int(p1_choice) < 0:
                    print(
                        "Your column needs to be between 0 and " + str((self.columns - 1)) + " but is actually " + str(
                            p2_choice) + ".")
                    continue

                if self.board.board_list[1][int(p2_choice) + 1] == self.character:
                    break
                else:
                    print("You cannot play in " + str(p2_choice) + " because it is full.")

            self._place_piece(int(p2_choice), self.player2.piece)
            if self._check_for_win(self.player2.piece):
                print(self.player2.name + " won the game!")
                break

            if self.character not in self.board.board_list[1]:
                print("Tie Game.")
                break
