import random
from Weapon import Weapon
from game_rules import GameRules

class GameBoard:

    def __init__(self):
        self.player = "Player"
        self.computer = "Computer"

    def play(self):
        Weapon.show_weapons()
        choice = int(input("Enter your choice (1-3): "))

        player_weapon = Weapon.get_weapon_by_choice(choice)
        computer_weapon = random.choice(Weapon.available_weapons)

        print(f"\nPlayer chose: {player_weapon}")
        print(f"Computer chose: {computer_weapon}")

        result = GameRules.decide_winner(player_weapon, computer_weapon)
        print("\nResult:", result)
