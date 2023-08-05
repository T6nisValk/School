testing_list = [0, 9, 8, 6, 4, 23, 3, 6, 4, 8, 2, 32, 9, 7, 41, 3, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 4,
                55, 6, 0, 68]

print(sorted(testing_list))


def selection(sortable):
    for index in range(0, len(sortable) - 1):
        min_value_index = index

        for j in range(index + 1, len(sortable) - 1):
            if sortable[j] < sortable[min_value_index]:
                min_value_index = j

        if min_value_index != index:
            sortable[min_value_index], sortable[index] = \
                sortable[index], sortable[min_value_index]
    return sortable


print(selection(testing_list))
