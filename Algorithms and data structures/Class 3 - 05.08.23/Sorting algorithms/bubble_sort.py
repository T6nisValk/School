testing_list = [0, 9, 8, 6, 4, 23, 3, 6, 4, 8, 2, 32, 9, 7, 41, 3, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 4,
                55, 6, 0, 68]

print(sorted(testing_list))


def bubble(sortable):
    indexing_length = len(sortable) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(0, indexing_length):
            if sortable[index] > sortable[index + 1]:
                is_sorted = False
                sortable[index], sortable[index + 1] = \
                    sortable[index + 1], sortable[index]
    return sortable


print(bubble(testing_list))
