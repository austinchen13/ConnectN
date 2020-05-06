from typing import List
class Board(object):
        def __init__(self, rows: int, columns: int, character: str) -> None:
            self.rows = rows
            self.columns = columns
            self.character = character
            self.new_character = str
            self.board_list: List[List[str]] = []

        def make_board_list(self) -> List[List[str]]:
            for i in range(0, self.rows + 1):
                self.board_list.append([])
            self.board_list[0].append(" ")
            for i in range(0, self.rows + 1):
                for j in range(0, self.columns):
                    if i == 0 and 0 <= j <= self.columns:
                        self.board_list[0].append(str(j))
                        continue
                    else:
                        self.board_list[i].append(str(i - 1))
                        for j in range(0, self.columns):
                            self.board_list[i].append(self.character)
                    break
            return self.board_list

        def __repr__(self) -> str:
            board_output = "  "
            for i in range(0, self.columns):
                if i == self.columns - 1:
                    board_output = board_output + str(i)
                    break
                board_output = board_output + str(i) + " "
            for i in range(0, self.rows):
                board_output = board_output + "\n"
                board_output = board_output + str(i) + " "
                for j in range(0, self.columns):
                    if j == self.columns - 1:
                        element = self.board_list[i + 1][j + 1]
                        board_output = board_output + element
                        break
                    element = self.board_list[i + 1][j + 1]
                    board_output = board_output + element + " "

            return board_output


