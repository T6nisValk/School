from random import choice
names = {
    "Aircraft Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2
}
y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

print(choice(y), choice(x))
