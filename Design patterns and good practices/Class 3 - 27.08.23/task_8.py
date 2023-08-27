from functools import reduce


def factorial(n):
    values = list(range(1, n + 1))
    result = reduce(lambda x, y: x * y, values)
    return result


user_input = int(input("Enter a number to get the factorial of it: "))
print(f"Factorial for number {user_input} is: {factorial(user_input)}")
