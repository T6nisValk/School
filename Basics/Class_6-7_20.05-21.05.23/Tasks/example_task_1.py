# Display the number 0.5 in the form of 1/2 - the correct implementation of str and repr is required.

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        pass


number = Rational(1, 5)
print(number)
