def factorial(n):
    # ITERATIVE MANNER
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(50))


def factorial_rec(n):
    # RECURSIVE MANNER
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


"""
    5 * factorial_rec(4)
    4 * factorial_rec(3)
    3 * factorial_rec(2)
    2 * factorial_rec(1)
    1 * factorial_rec(0) => returns 1 => 1 * 1
"""

print(factorial_rec(50))
