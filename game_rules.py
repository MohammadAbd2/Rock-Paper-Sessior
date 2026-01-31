class GameRules:

    @staticmethod
    def decide_winner(player_weapon, computer_weapon):
        if player_weapon == computer_weapon:
            return "Draw"

        if (
            (player_weapon == "Rock" and computer_weapon == "Scissors") or
            (player_weapon == "Paper" and computer_weapon == "Rock") or
            (player_weapon == "Scissors" and computer_weapon == "Paper")
        ):
            return "Player Wins!"

        return "Computer Wins!"
