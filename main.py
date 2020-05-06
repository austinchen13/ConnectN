import sys
from typing import Dict, Union
from ConnectNGame.src.game import Game


def main() -> None:
    config_dict: Dict[str, str] = {}
    config_file = sys.argv[1]
    with open(config_file) as file:
        for line in file:
            line = line.split(":") # type: ignore
            key = line[0]
            key = key.strip()
            value = line[1]
            value = value.strip()
            config_dict[key] = value

    num_rows = int(config_dict["num_rows"])
    num_columns = int(config_dict["num_cols"])
    num_pieces_to_win = int(config_dict["num_pieces_to_win"])
    blank_char = config_dict["blank_char"]
    play_game = Game(num_rows, num_columns, num_pieces_to_win, blank_char)
    play_game.make_two_players()
    play_game.initialize_game()
    play_game.play()


if __name__ == '__main__':
    main()
