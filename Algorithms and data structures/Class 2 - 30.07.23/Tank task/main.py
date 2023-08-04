import random
import keyboard


class Tank:
    def __init__(self):
        self.coordinates = {"X": 0, "Y": 0}
        self.direction = "UP"
        self.amount_of_shots = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}
        self.my_points = 0

    def move(self, move):
        self.my_points -= 10
        if move == "FORWARD".lower():
            print(f"\n--------------------\n"
                  f"Tank moved {move}.\n"
                  f"--------------------")
            if self.direction == "UP":
                self.coordinates["Y"] += 1
            elif self.direction == "DOWN":
                self.coordinates["Y"] -= 1
            elif self.direction == "RIGHT":
                self.coordinates["X"] += 1
            elif self.direction == "LEFT":
                self.coordinates["X"] -= 1
        elif move == "BACK".lower():
            print(f"\n--------------------\n"
                  f"Tank moved {move}.\n"
                  f"--------------------")
            if self.direction == "UP":
                self.coordinates["Y"] -= 1
                self.direction = "DOWN"
            elif self.direction == "DOWN":
                self.coordinates["Y"] += 1
                self.direction = "UP"
            elif self.direction == "RIGHT":
                self.coordinates["X"] -= 1
                self.direction = "LEFT"
            elif self.direction == "LEFT":
                self.coordinates["X"] += 1
                self.direction = "RIGHT"
        elif move == "RIGHT".lower():
            print(f"\n--------------------\n"
                  f"Tank moved {move}.\n"
                  f"--------------------")
            if self.direction == "UP":
                self.coordinates["X"] += 1
                self.direction = "RIGHT"
            elif self.direction == "DOWN":
                self.coordinates["X"] -= 1
                self.direction = "LEFT"
            elif self.direction == "RIGHT":
                self.coordinates["Y"] -= 1
                self.direction = "DOWN"
            elif self.direction == "LEFT":
                self.coordinates["Y"] += 1
                self.direction = "UP"
        elif move == "LEFT".lower():
            print(f"\n--------------------\n"
                  f"Tank moved {move}.\n"
                  f"--------------------")
            if self.direction == "UP":
                self.coordinates["X"] -= 1
                self.direction = "LEFT"
            elif self.direction == "DOWN":
                self.coordinates["X"] += 1
                self.direction = "RIGHT"
            elif self.direction == "RIGHT":
                self.coordinates["Y"] += 1
                self.direction = "UP"
            elif self.direction == "LEFT":
                self.coordinates["Y"] -= 1
                self.direction = "DOWN"

    def shoot(self, target):
        self.amount_of_shots[self.direction] += 1
        if target.coordinates["Y"] == self.coordinates["Y"]:
            if (target.coordinates["X"] < self.coordinates["X"]) and self.direction == "LEFT":
                target.alive = 0
                target.amount_of_target_deaths += 1
                self.my_points += 100
                print("\n--------------------\n"
                      "Direct hit!\n"
                      "--------------------")

            elif (target.coordinates["X"] > self.coordinates["X"]) and self.direction == "RIGHT":
                target.alive = 0
                target.amount_of_target_deaths += 1
                self.my_points += 100
                print("\n--------------------\n"
                      "Direct hit!\n"
                      "--------------------")
            else:
                self.my_points -= 20
                print("\n--------------------\n"
                      "You missed\n"
                      "--------------------")

        elif target.coordinates["X"] == self.coordinates["X"]:
            if (target.coordinates["Y"] < self.coordinates["Y"]) and self.direction == "DOWN":
                target.alive = 0
                target.amount_of_target_deaths += 1
                self.my_points += 100
                print("\n--------------------\n"
                      "Direct hit!\n"
                      "--------------------")

            elif (target.coordinates["Y"] > self.coordinates["Y"]) and self.direction == "UP":
                target.alive = 0
                target.amount_of_target_deaths += 1
                self.my_points += 100
                print("\n--------------------\n"
                      "Direct hit!\n"
                      "--------------------")
            else:
                self.my_points -= 20
                print("\n--------------------\n"
                      "You missed\n"
                      "--------------------")
        else:
            self.my_points -= 20
            print("\n--------------------\n"
                  "You missed\n"
                  "--------------------")

    def info(self):
        print(f"\n--------------------\n"
              f"Tank is facing: {self.direction}\n"
              f"Tanks coordinates are: {self.coordinates}\n"
              f"Shots to each direction: {self.amount_of_shots}\n"
              f"Total number of shots: {sum(self.amount_of_shots.values())}\n"
              f"--------------------")

    def points(self):
        print(f"\n--------------------\n"
              f"Your points: {self.my_points}\n"
              f"--------------------")


class Target:
    def __init__(self):
        self.coordinates = {}
        self.alive = 0
        self.amount_of_target_deaths = 0

    def spawn_target(self, my_tank):
        self.alive = 1
        self.coordinates = {
            "X": random.randint(*random.choice([(-10, my_tank["X"] - 1),
                                                (my_tank["X"] + 1, 10)])),
            "Y": random.randint(*random.choice([(-10, my_tank["Y"] - 1),
                                                (my_tank["Y"] + 1, 10)]))
        }

    def location(self):
        print(f"\n--------------------\n"
              f"Target is located at:\n"
              f"{self.coordinates}\n"
              f"--------------------\n")


def start_game():
    while True:

        print("1 to play a new game,\n"
              "2 to see previous scores,\n"
              "ESC to exit the game.")
        player_input = keyboard.read_event()
        if player_input.name == "1" and player_input.event_type == "down":
            break
        elif player_input.name == "esc" and player_input.event_type == "down":
            exit()
        elif player_input.name == "2" and player_input.event_type == "down":
            with open("player_scores.txt") as f:
                for line in f.readlines():
                    print(line, end="")


def tank_control():
    my_tank = Tank()
    target = Target()
    target.spawn_target(my_tank.coordinates)
    start_game()
    print("--------------------"
          "Welcome to the game!\n"
          "Use the WASD keys to move the tank and space to shoot.\n"
          "1 to see player info,\n"
          "2 to see target info,\n"
          "3 to see your current score,\n"
          "ESC to exit the game.\n"
          "Destroy 10 targets to end the game.\n"
          "--------------------")

    while True:
        if target.amount_of_target_deaths == 10:
            print(f"\n--------------------\n"
                  f"Game over!\n"
                  f"You killed {target.amount_of_target_deaths} targets.\n"
                  f"Your total score: {my_tank.my_points}\n"
                  f"--------------------")
            player_name = input("Enter your name: ")
            with open("player_scores.txt", "a") as f:
                f.write(f"{player_name}: {my_tank.my_points}\n")
            exit()

        player_input = keyboard.read_event()
        if player_input.name == "space" and player_input.event_type == "down":
            my_tank.shoot(target)
            if target.alive == 0:
                target.spawn_target(my_tank.coordinates)
            continue
        elif player_input.name == "1" and player_input.event_type == "down":
            my_tank.info()
            continue
        elif player_input.name == "2" and player_input.event_type == "down":
            target.location()
            continue
        elif player_input.name == "3" and player_input.event_type == "down":
            my_tank.points()
        elif player_input.name == "w" and player_input.event_type == "down":
            my_tank.move("forward")
        elif player_input.name == "s" and player_input.event_type == "down":
            my_tank.move("back")
        elif player_input.name == "d" and player_input.event_type == "down":
            my_tank.move("right")
        elif player_input.name == "a" and player_input.event_type == "down":
            my_tank.move("left")

        elif player_input.name == "esc" and player_input.event_type == "down":
            print("Thank you for playing")
            break

    exit()


tank_control()
