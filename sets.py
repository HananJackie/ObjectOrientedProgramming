import random

AMOUNT_OF_NUMBERS = 10
has_won = False
counter = 0
while not has_won:
    guessed_lottery_numbers = {random.randint(1,45) for i in range(AMOUNT_OF_NUMBERS)}
    actual_lottery_numbers = {random.randint(1,45) for i in range(AMOUNT_OF_NUMBERS)}
    if len(guessed_lottery_numbers.intersection(actual_lottery_numbers)) == AMOUNT_OF_NUMBERS:
        print("yay!")
        has_won = True



print(counter)
