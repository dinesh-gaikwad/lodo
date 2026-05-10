from django.test import TestCase
from .game_logic import LudoGame

class LudoGameTest(TestCase):

    def setUp(self):
        self.game = LudoGame()
        self.game.add_player("Player1")

    def test_roll_dice(self):
        value = self.game.roll_dice()
        self.assertTrue(1 <= value <= 6)

    def test_move_player(self):
        position = self.game.move_player(0, 5)
        self.assertEqual(position, 5)

    def test_winner(self):
        self.game.move_player(0, 100)
        self.assertTrue(self.game.check_winner(0))
