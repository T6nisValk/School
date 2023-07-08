# Examples.
import math


def valid_prime_number(x):
    if x <= 1:
        return False
    for number in range(2, int(math.sqrt(x)) + 1):
        if x % number == 0:
            return False
    return True


def prime_generator(n):
    for i in range(n):
        if valid_prime_number(i):
            yield i


print(list(prime_generator(25)))

"""
Fibonacci Series - each number is the sum of 2 previous numbers:
0, 1, 2, 3, 5, 8, 13 ...
"""


def fibonacci(n):
    a, b = 0, 1
    counter = 0
    while True:
        if counter >= n:
            break
        yield a
        a, b = b, a + b
        counter += 1


# fib = fibonacci(20)
# for x in fib:
#     print(x)
print(list(fibonacci(20)))  # Prints a list of values


def square(n):
    for num in n:
        yield num ** 2


chained = square(fibonacci(20))
print([c for c in chained])
