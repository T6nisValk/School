class Animal:
    # __init__ Constructor for the class
    # self represents the instance of a variable
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    # Methods
    def walk(self):
        print(f"{self.name} is walking with {self.legs} legs")


# Objects
cat = Animal("Pähkel", 4)
dog = Animal("Jack", 4)

cat.walk()
