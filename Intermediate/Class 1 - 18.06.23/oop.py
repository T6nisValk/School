# Abstract class
# Square, rectangle, parallelogram
# They have some attributes in common: Area, Perimeter
# We can create abstract class for the commonality between our objects

# To create an abstract class, import abc
# Abstract Base Class

from abc import ABC, abstractmethod


class FourSidedObjects(ABC):
    # This is a decorator, it means that the method is an abstract method
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(FourSidedObjects):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return self.length * 4


sqr = Square(5)
print(sqr.area())
print(sqr.perimeter())
