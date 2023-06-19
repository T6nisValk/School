# The comparison methods (eq, lt, gt, le, ge, cmp) should take � = 2/4.

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


number = Rational(1, 5)
number2 = Rational(2, 5)
print(number.__eq__(number2))  # print(number == number2)
print(number.__lt__(number2))  # print(number < number2)
print(number.__gt__(number2))  # print(number > number2)
print(number.__le__(number2))  # print(number <= number2)
print(number.__ge__(number2))  # print(number >= number2)

