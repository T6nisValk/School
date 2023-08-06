from random import choice
names = {
    "Aircraft Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2
}
y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


class Warship:
    def __init__(self, name, starting_coordinate, direction):
        self.name = name
        self.coordinates = [starting_coordinate]  # [B2, B3, B4, B5, B6]
        self.length = names[name]
        self.destroyed = []
        self.is_valid = True

        for _ in range(self.length-1):
            current_last_coordinate = self.coordinates[-1]
            index_of_y = y.index(current_last_coordinate[:1])
            index_of_x = x.index(current_last_coordinate[1:])
            if direction.upper() == "D":
                index_of_y += 1
            elif direction.upper() == "U":
                index_of_y -= 1
            elif direction.upper() == "L":
                index_of_x -= 1
            elif direction.upper() == "R":
                index_of_x += 1

            if (index_of_y > 9 or index_of_y < 0) or (index_of_x > 9 or index_of_x < 0):
                self.is_valid = False
            else:
                self.coordinates.append(f"{y[index_of_y]}{x[index_of_x]}")

    def __repr__(self) -> str:
        return f"{self.coordinates}"

    def is_destroyed(self):
        return sorted(self.coordinates) == sorted(self.destroyed)


class Board:
    def __init__(self):
        self.missed_shots = []
        self.made_shots = []
        self.ships = []
        self.destroyed_ships = []

    def register_ship(self, ship):
        for existing in self.ships:
            for coordinate in ship.coordinates:
                if coordinate in existing.coordinates:
                    return False
        self.ships.append(ship)
        return True

    def all_ships_destroyed(self):

        return len(self.destroyed_ships) == len(self.ships)

    def shoot(self, coordinate, who):
        is_missed = True
        for ship in self.ships:
            if coordinate in ship.coordinates:
                if coordinate not in ship.destroyed:
                    is_missed = False
                    self.made_shots.append(coordinate)
                    ship.destroyed.append(coordinate)
                    print(f"{who} hit a ship at {coordinate}")
                    if ship.is_destroyed():
                        print(f"{ship.name} is destroyed.")
                        self.destroyed_ships.append(ship)
                    return True
                else:
                    print(
                        "Can not shoot to the same place twice, you already destroyed this part of the ship")
                    return False
        if is_missed:
            self.missed_shots.append(coordinate)
            print(f"{who} missed at {coordinate}")
            return True


enemy_board = Board()
directions = ["L", "R", "U", "D"]
for name in names.keys():
    status_of_registration = False
    while not status_of_registration:
        warship = Warship(name, "A1", "U")
        while not warship.is_valid:
            starting_coordinate = f"{choice(y)}{choice(x)}"
            direction = choice(directions)
            warship = Warship(name, starting_coordinate, direction)
            if not warship.is_valid:
                pass
        status_of_registration = enemy_board.register_ship(warship)
        if not status_of_registration:
            pass
print(enemy_board.ships)
print("Hello Sir, setup your board.")

user_board = Board()
for name in names.keys():
    status_of_registration = False
    while not status_of_registration:
        warship = Warship(name, "A1", "U")
        while not warship.is_valid:
            starting_coordinate = input(
                f"Provide starting coordinate(A-J, 1-10) for the ship: {name}\n").upper()
            direction = input("L - LEFT\nR - RIGHT\nU - UP\nD - DOWN\n")
            warship = Warship(name, starting_coordinate, direction)
            if not warship.is_valid:
                print("Cant place the Warship there, try again:")
        status_of_registration = user_board.register_ship(warship)
        if not status_of_registration:
            print("The Warships can not overlap, try again:")


print("-----------------------The board is now setup, the game may start.-------------------------")

while not (user_board.all_ships_destroyed() or enemy_board.all_ships_destroyed()):
    user_shot = False
    enemy_shot = False
    while not user_shot:
        print(enemy_board.ships)
        target = input(
            "It your time to take a shot, enter the coordinates to shoot:")
        user_shot = enemy_board.shoot(target.upper(), "Player")
    while not enemy_shot:
        enemy_target = f"{choice(y)}{choice(x)}"
        enemy_shot = user_board.shoot(enemy_target, "Enemy")
if user_board.all_ships_destroyed():
    print("AI for the win.")
elif enemy_board.all_ships_destroyed():
    print("Suck it AI, I won.")
