# Adding 15 to a number passed in an argument.


def add_15(x):
    return x + 15


print(add_15(20))

sum_15 = lambda x: x + 15
print(sum_15(10))

# Get products/multiplication of numbers

multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))


# Lambda functions inside normal/other functions


def multiply_results(n):
    return lambda a: a * n


tripler = multiply_results(5)  # Value for n
print(tripler(5))  # Value for a


# Get the even numbers in a list


def get_even(nums):
    evens = []
    for item in nums:
        if item % 2 == 0:
            evens.append(item)
    return evens


my_list = [2, 3, 4, 5, 6, 7, 8]
print(get_even(my_list))

even = lambda x: [num for num in x if num % 2 == 0]
print(even(my_list))


# String actions


def yell(s):
    return s.upper()


print(yell("hello"))

yell_1 = lambda s: s.upper()
print(yell_1("hello"))
