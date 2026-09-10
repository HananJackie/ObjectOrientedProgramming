from enum import Enum

class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Game:
    def __init__(self, name, level: Level, price):
        self.name = name
        self.level = level
        self.price = price

    def print_info(self):
        print(f"Game: {self.name}")
        print(f"Level: {self.level.name}")
        print(f"price: {self.price}")

if __name__ == "__main__":
    g = Game('Terraria', Level.HARD, 100.2)
    g.print_info()