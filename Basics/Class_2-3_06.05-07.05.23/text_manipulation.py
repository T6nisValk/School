
# [ START : STOP : STEP ]

text_variable = "Bad dog"
print("Our string variable is", text_variable)
# Length of the string variable
# Prints the length of the string.
print("\nLength of the string is", len(text_variable))
# Index of the "FIRST" letter in the string variable
print("\nThe first index of a letter d is", text_variable.index("d"))
# Number of occurrences in the string valuable
print("\nThe amount of times letter d shows up in", text_variable.count("d"))
# Get the letter by index
print("\nIn the index 2 in this variable the letter is", text_variable[2])
# Range of values by index
print("\nLetters between 0 to 7 index are", text_variable[0:7])
#  Range value with step
print("\nLetters between 0 to 7 index stepped by 2 are",
      text_variable[0:7:2])  # :2 gives 2 steps
print("Every second value", text_variable[::2])
print("Every second value backwards", text_variable[::-2])
print("The string variable backwards", text_variable[::-1])
# Lower and upper case
print("All lower case", text_variable.lower())
print("All upper case", text_variable.upper())
