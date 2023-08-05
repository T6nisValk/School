testing_list = [0, 9, 8, 6, 4, 23, 3, 6, 4, 8, 2, 32, 9, 7, 41, 3, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 4,
                55, 6, 0, 68]

print(sorted(testing_list))


def merge(sortable):
    if len(sortable) > 1:
        mid = len(sortable) // 2
        left_side = sortable[:mid]
        right_side = sortable[mid:]

        merge(left_side)
        merge(right_side)

        i = 0
        j = 0
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                sortable[k] = left_side[i]
                i += 1
            else:
                sortable[k] = right_side[j]
                j += 1

            k += 1
        while i < len(left_side):
            sortable[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            sortable[k] = right_side[j]
            j += 1
            k += 1

    return sortable


print(merge(testing_list))
