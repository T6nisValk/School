# Task 5: Write a Python program that accepts a word from the user, reverses it and prints it.

user_input = input("Enter a word: ")

reversed_user_input = user_input[::-1]
for index, char in enumerate(reversed_user_input):
    if index == 0:
        print(f"{char.upper()}", end="")
    else:
        print(char.lower(), end="")
