# Create a class called "Rectangle" with attributes for length and width.
# Add a method to the Rectangle class that calculates and returns the area.
# Create a subclass of Rectangle called "Square" that automatically sets the length and width to be equal.
# Add a method to the Square class that calculates and returns the perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return float(self.length * self.width)


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        average = (self.length + self.width) / 2
        self.length = average
        self.width = average

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(5, 6)
print(f"Rectangles area is: {rectangle.area()}")

square = Square(5, 6)
print(f"Rectangle made to a square and it's perimeter is: {square.perimeter()}")
