
class Player(object):
    def __init__(self, name : str, piece : str) -> None:
        self.name = name
        self.piece = piece

    def __str__(self) -> str:
        return self.name




