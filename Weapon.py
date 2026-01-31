class Weapon:
    available_weapons = ["Rock", "Paper", "Scissors"]

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_weapons(cls):
        print("Choose your weapon:")
        for index, weapon in enumerate(cls.available_weapons):
            print(f"{index + 1}. {weapon}")

    @classmethod
    def get_weapon_by_choice(cls, choice):
        return cls.available_weapons[choice - 1]




