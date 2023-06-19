""" sum numbers until flag -9999 is seen

methods:

You can save the numbers in a list and compute
You can use positional arguments
You can use while loop """

nums = [1, 2, 3, 4, 5, 6, -9999, 7, 8, 9]


def sum_nums(numbers):
    summed = 0
    for x in numbers:
        if x != -9999:
            summed += x
        else:
            break
    return summed


print(sum_nums(nums))
