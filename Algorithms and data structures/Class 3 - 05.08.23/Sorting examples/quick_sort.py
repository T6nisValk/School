testing_list = [0, 9, 8, 6, 4, 23, 3, 6, 4, 8, 2, 32, 9, 7, 41, 3, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 4,
                55, 6, 0, 68]

print(sorted(testing_list))


def quick(sortable):
    length = len(sortable)
    if length <= 1:
        return sortable
    else:
        pivot = sortable.pop()

        greater_values = []
        lower_values = []

        for item in sortable:
            if item > pivot:
                greater_values.append(item)
            else:
                lower_values.append(item)

    return quick(lower_values) + [pivot] + quick(greater_values)


print(quick(testing_list))
