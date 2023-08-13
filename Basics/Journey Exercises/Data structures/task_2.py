tensor = [
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
]


def flatten(hashed):
    result = []
    for up in hashed:
        for middle in up:
            for low in middle:
                result.append(low)

    return result


print(flatten(tensor))
