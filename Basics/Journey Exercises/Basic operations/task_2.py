import math


def preceded_by_prime(number):
    def valid_prime_number(x):
        if x <= 1:
            return False
        for num in range(2, int(math.sqrt(x)) + 1):
            if x % num == 0:
                return False
        return True

    if valid_prime_number(number - 1):
        return True
    else:
        return False
