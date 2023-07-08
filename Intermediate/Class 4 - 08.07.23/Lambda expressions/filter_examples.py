import math

# Filter filters out numbers from a list when the function returns True
numbers = [234, 4, 4, 25, 26, 23, 4, 6, 2, 42, 53]
greater_than_20 = list((filter(lambda x: x > 20, numbers)))
print(greater_than_20)

# Return prime numbers
"""
Prime number is a number that is divisible by 1 and itself.
"""


def valid_prime_number(x):
    if x <= 1:
        return False
    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return False
    return True


primes = list(filter(valid_prime_number, range(1, 100)))
print(primes)

# Palindrome.
"""
A palindrome is a word or a sentence that's the same when read backwards.
"""


def valid_palindrome(x):
    return x.lower() == x[::-1].lower()


words = ["Hello", "Hannah", "racecar", "madam", "blue"]
palindromes = list(filter(valid_palindrome, words))
print(palindromes)
