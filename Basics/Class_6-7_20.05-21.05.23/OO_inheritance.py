class Animal:
    def __init__(self, type_):
        self.type = type_

    def move(self):
        print(self.type + " is moving")


class Mammal(Animal):
    def __init__(self, legs):
        super().__init__(type_="Mammal")
        self.legs = legs


class ColdBlood(Animal):
    def __init__(self, legs):
        super().__init__(type_="ColdBlood")
        self.legs = legs


human = Mammal(4)
print(human.type)
raptor = ColdBlood(legs=4)
print(raptor.legs)
raptor.move()
human.move()
