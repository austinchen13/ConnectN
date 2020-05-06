import unittest
from ConnectNGame.src.player import Player


class TestPlayer(unittest.TestCase):
    def test_creating_player(self):
        a = Player("Bob", "x")
        self.assertEqual(a.name, "Bob")
        self.assertEqual(a.piece, "x")

    def test_str(self):
        a = Player("Austin", "p")
        self.assertEqual(str(a), "Austin")

    def test_multiple_creations(self):
        p1 = Player("Bob", "x")
        p2 = Player("Austin", "o")
        self.assertNotEqual(p1.name, "Austin")
        self.assertNotEqual(p2.name, "Bob")
        self.assertEqual(p1.name, "Bob")
        self.assertEqual(p2.name, "Austin")
        self.assertNotEqual(p2.piece, "x")



if __name__ == '__main__':
    unittest.main()
