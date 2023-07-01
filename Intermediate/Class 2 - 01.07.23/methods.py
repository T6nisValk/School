
class Hello:
    default_name = "Merily"

    def __init__(self, name):
        self.name = name
    """
    This is an instance method. First parameter is "self"
    """

    def say_hello(self):
        return f"{self.name}, enchante"

    @classmethod
    def class_example(cls):
        print("This is a class method example.")


# Instance method
var1 = Hello("T6nis")
print(var1.say_hello())
print(var1.name)  # I can access the instance variable
var2 = Hello("P2hkel")
print(var2.say_hello())
# Class method - Don't need to create an object
Hello.class_example()
print(Hello.default_name)  # Can only access a class global variable


class Weight:
    def __init__(self, weight_kg, height_m):
        self.weight = weight_kg
        self.height = height_m

    def bmi(self):
        return self.weight / self.height**2

    @classmethod
    def convert_to_pounds(cls, weight_kg):
        return weight_kg * 2.205

    @classmethod
    def convert_to_kg(cls, weight_kg):
        return weight_kg / 2.205

    @staticmethod
    def info():
        print("This is a static method example:\n"
              "<This class computes BMI>")


mina = Weight(75, 1.83)
print(mina.bmi())
print(Weight.convert_to_pounds(mina.weight))
Weight.info()
