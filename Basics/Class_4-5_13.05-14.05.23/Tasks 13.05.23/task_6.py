# Task 6: Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


def odd_even(*args):
    even_num = 0
    odd_num = 0
    for number in args:
        if number % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    print(f"Number of even numbers: {even_num}\n" f"Number of odd numbers: {odd_num}")


odd_even(5, 6, 6, 6, 6, 5, 5)
