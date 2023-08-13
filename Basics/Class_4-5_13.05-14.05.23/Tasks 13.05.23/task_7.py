# Task 7: Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
def count_letters_and_digits(text):
    letters = 0
    digits = 0
    rest_of_the_stuff = 0
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            rest_of_the_stuff += 1
    print(
        f"Letters: {letters}\n"
        f"Digits: {digits}\n"
        f"Rest of the stuff(spaces, dots, commas, etc.: {rest_of_the_stuff}"
    )


count_letters_and_digits("Python 3.2")
