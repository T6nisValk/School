# Examples
import math

# Read file with for loop
with open("readme.txt") as f:
    for line in f:
        print(line, end="")
# Iter example.
cities = ["P2rnu", "Tartu", "Tallinn"]
cities_iter = iter(cities)
print(f"First iterable: {next(cities_iter)}\n"
      f"Second iterable: {next(cities_iter)}\n"
      f"Third iterable: {next(cities_iter)}\n")
# print(f"Error: {next(cities_iter)}") - Throws an error, because there are no more items in list.


"""
Creating an iterable:
- __init__
- __iter__
- __next__
"""


# This is basically a range() function.
class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


for num in MyIterable(1, 14):
    print(num)

# Example Cycle
"""
Iterate through a list or string until stopped.
hello => return h, e, l, l, o, h, e, l, l, o ... until I tell it to stop.
"""


class CycleIterable:
    def __init__(self, value):
        self.value = iter(value)
        self.iterable = value

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                next_object = next(self.value)
                return next_object
            except StopIteration:
                self.value = iter(self.iterable)


c = CycleIterable("Hello")
for i in range(15):
    print(next(c))


def valid_prime_number(x):
    if x <= 1:
        return False
    for number in range(2, int(math.sqrt(x)) + 1):
        if x % number == 0:
            return False
    return True


def get_n_prime_numbers(n):
    prime = []
    for item in range(2, n):
        if valid_prime_number(item):
            prime.append(item)
    return prime


values = get_n_prime_numbers(25)
print(values)


# Prime iterator class

class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num >= self.n:
            raise StopIteration
        elif valid_prime_number(self.num):
            return self.num
        # Default else - go to the next number
        return self.__next__()


value = PrimeIterator(25)
print([num for num in value])
