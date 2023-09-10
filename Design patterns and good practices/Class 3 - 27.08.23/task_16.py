import math


def valid_prime_number(x):
    if x <= 1:
        return False
    for number in range(2, int(math.sqrt(x)) + 1):
        if x % number == 0:
            return False
    return True


def prime_generator():
    number = 0
    while True:
        if valid_prime_number(number):
            yield number
        number += 1


primes = prime_generator()
for _ in range(10):
    print(next(primes))
