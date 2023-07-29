def to_weird_case(_string):
    index = 0  # Using enumerate also indexes non-characters.
    result = ""
    for character in _string:
        if character.isalpha():
            if index % 2 != 0:
                result += character.lower()
            else:
                result += character.upper()
            index += 1
        else:
            result += " "
    return result


print(to_weird_case("String"))
print(to_weird_case('Algorithms and data structures'))
