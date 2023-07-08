# To use reduce() we have to import it from functools.
from functools import reduce


# Add all the numbers in a list

def addition(x, y):
    return x + y


def product(x, y):
    return x * y


my_list = [2, 3, 4, 5, 6, 7, 8]
added_numbers = reduce(addition, my_list)  # reduce(lambda x, y: x+y, my_list)
multiply_numbers = reduce(product, my_list)
print(multiply_numbers)
print(added_numbers)

# Get macimum number in a list
num_list = [123, 44, 2, 15, 13, 333, 4]
max_num = reduce(lambda a, b: a if a > b else b, num_list)
print(max_num)

# print(max(num_list)) - Also an option to get the max number.

# Filter then reduce
list_sum = [1, 2, 3, 4, 5, 6]


def sum_even(nums):
    return sum(num for num in nums if num % 2 == 0)


print(sum_even(list_sum))

evens = list(filter(lambda x: x % 2 == 0, list_sum))
sum_of_evens = reduce(lambda x, y: x + y, evens)
print(sum_of_evens)

combined = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, list_sum))
print(combined)

# Get the total in a dictionary.
groceries = [
    {"item": "bread", "price": 1.3},
    {"item": "milk", "price": 2},
    {"item": "apple", "price": 0.56}
]
"""
x = Accumulated value
y = Current dictionary value
Third parameter is the initializer which serves as a default value if the second parameter y is 
an empty sequence.
"""
total_cost = reduce(lambda x, y: x + y["price"], groceries, 0)
print(f"{total_cost} EUR")
