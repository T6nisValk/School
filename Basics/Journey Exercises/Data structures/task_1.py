import random

picked_numbers = {}


def random_number(x):
    if x in picked_numbers:
        return f"Oh no, I repeated myself, number {x} is already picked."
    else:
        picked_numbers[x] = 1
        return f"Number {x} added to the list."


x = 10
while x > 0:
    x -= 1
    print(random_number(random.randint(0, 10)))
