def swap_case(text):
    result = ""
    for char in text:
        if char.isupper():
            result += char.lower()

        else:
            result += char.upper()
    return result


def shortest_word(text):
    shortest = ''
    length = 99

    words = text.strip().split(' ')
    for word in words:
        if len(word) < length:
            length = len(word)
            shortest = word
    return shortest
