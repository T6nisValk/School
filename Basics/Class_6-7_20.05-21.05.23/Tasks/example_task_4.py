# The operators +, -, *, / should be implemented correctly and return a new object of this class.

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # ---------------- Task 1--------------------------------------------------------
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        pass

    # ---------------- Task 2--------------------------------------------------------
    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __invert__(self):
        return Rational(self.denominator, self.numerator)

    # ---------------- Task 3--------------------------------------------------------
    def __eq__(self, other):
        # if self.denominator == other.denominator and self.numerator == other.numerator:
        #     return True
        # else:
        #     return False
        return self.numerator * self.denominator == other.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * self.denominator < other.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * self.denominator > other.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * self.denominator <= other.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * self.denominator >= other.denominator * other.numerator

    # ---------------- Task 4--------------------------------------------------------
    def __add__(self, other):
        return Rational(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)
    # numerator = self.numerator * other.denominator + self.denominator * other.numerator
    # denominator = self.denominator * other.denominator
    # return Rational(numerator, denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)
    # numerator = self.numerator * other.denominator - self.denominator * other.numerator
    # denominator = self.denominator * other.denominator
    # return Rational(numerator, denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
    # numerator = self.numerator * other.numerator
    # denominator = self.denominator * other.denominator
    # return Rational(numerator, denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    # numerator = self.numerator * other.denominator
    # denominator = self.denominator * other.numerator
    # return Rational(numerator, denominator)

number = Rational(1, 2)
number2 = Rational(2, 5)
print(number.__add__(number2))  # print(number + number2)
print(number.__sub__(number2))  # print(number - number2)
print(number.__mul__(number2))  # print(number * number2)
print(number.__truediv__(number2))  # print(number / number2)
