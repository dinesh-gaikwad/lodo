import unittest
from apps.ludo.game_logic import LudoGame

class TestLudoGame(unittest.TestCase):

    def setUp(self):
        self.game = LudoGame()

        self.game.add_player("Player1")
        self.game.add_player("Player2")

    def test_player_creation(self):
        self.assertEqual(len(self.game.players), 2)

    def test_dice_roll(self):
        value = self.game.roll_dice()

        self.assertTrue(1 <= value <= 6)

    def test_player_move(self):
        position = self.game.move_player(0, 5)

        self.assertEqual(position, 5)

    def test_max_position(self):
        position = self.game.move_player(0, 150)

        self.assertEqual(position, 100)

    def test_winner(self):
        self.game.move_player(0, 100)

        self.assertTrue(self.game.check_winner(0))

    def test_turn_system(self):
        current = self.game.next_turn()

        self.assertEqual(current, 1)

    def test_multiple_turns(self):
        self.game.next_turn()
        current = self.game.next_turn()

        self.assertEqual(current, 0)

if __name__ == "__main__":
    unittest.main()
