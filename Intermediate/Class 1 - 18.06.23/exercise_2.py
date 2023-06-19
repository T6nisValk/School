# given 2 strings, can you make first string from the second by deleting some characters


s1 = "Hello"
s2 = "vufigsaHudesdflelio"


def string_creation(string1, string2):
    counter = 0
    for char in string1.lower():
        if char in string2.lower():
            counter += 1
    if counter == len(string1):
        print(True)


string_creation(s1, s2)
