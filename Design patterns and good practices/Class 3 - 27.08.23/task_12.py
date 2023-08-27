from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_area(self, radius):
        return round(pi * (radius**2), 2)


class Rectangle(Shape):
    def calculate_area(self, width, length):
        return width * length


circle = Circle()
rectangle = Rectangle()

print(f"Circle area: {circle.calculate_area(5)}")
print(f"Rectangle area: {rectangle.calculate_area(5, 5)}")
