import random

class AIBot:

    def __init__(self, name="Bot"):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def make_move(self):
        dice = self.roll_dice()
        self.position += dice

        if self.position > 100:
            self.position = 100

        return {
            "dice": dice,
            "position": self.position
        }
