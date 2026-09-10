from enum import Enum

class Medals(Enum):
    GOLD = 1
    SILVER = 2
    BRONZE = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


if __name__ == "__main__":
    medal = Medals.BRONZE

    match medal:
        case Medals.GOLD:
            print('1st place')
        case Medals.SILVER:
            print('2nd place')
        case Medals.BRONZE:
            print('3rd place')
        case _:
            print('not possible')

    orders = ['st', 'nd', 'rd']
    for medal in Medals:
        print(f'{medal.name} is {medal.value}{orders[medal.value-1]} place')
