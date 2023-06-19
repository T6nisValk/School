# The float method should return a decimal number,
# and int should be similar to its counterpart in the case of float numbers.
# Additionally, the invert method should be used.

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    # Task 1
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        pass
    # Task 2
    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __invert__(self):
        return Rational(self.denominator, self.numerator)


number = Rational(1, 5)
print(number.__float__())  # print(float(number))
print(number.__int__())  # print(int(number))
print(number.__invert__())  # print(~number)