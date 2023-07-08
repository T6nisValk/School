# Square the content of a list

list_c = [2, 3, 4, 5, 6]
squared = list(map(lambda x: x ** 2, list_c))  # Map applies the function to all variables in an
# iterable

print(squared)

# Determine whether a number is odd or even. If even, return True

even_odd = list(map(lambda x: x % 2 == 0, [2, 3, 4]))
print(even_odd)
# Get the length of each string in a list
words = ["Thankful", "Bonne nuit", "Devant"]
word_list = list(map(lambda x: len(x), words))
print(word_list)


def word_length(word):
    return len(word)


word_list_b = list(map(word_length, words))
print(word_list_b)
