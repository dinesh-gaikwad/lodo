import random

class LudoGame:

    def __init__(self):
        self.players = []
        self.current_turn = 0

    def add_player(self, player):
        self.players.append({
            "name": player,
            "position": 0
        })

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_index, steps):
        self.players[player_index]["position"] += steps

        if self.players[player_index]["position"] > 100:
            self.players[player_index]["position"] = 100

        return self.players[player_index]["position"]

    def check_winner(self, player_index):
        return self.players[player_index]["position"] >= 100

    def next_turn(self):
        self.current_turn += 1

        if self.current_turn >= len(self.players):
            self.current_turn = 0

        return self.current_turn
