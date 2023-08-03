book_pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
page_we_want = 20
amount_of_times = 0


def binary_search_iter(array, find_x_in_array):
    low = 0
    high = len(array) - 1
    global amount_of_times
    while low <= high:
        amount_of_times += 1
        mid = (low + high) // 2
        if array[mid] < find_x_in_array:
            low = mid + 1
        elif array[mid] > find_x_in_array:
            high = mid - 1
        else:
            return mid
    return -1


print(f"Index for {page_we_want} in {book_pages} is "
      f"{binary_search_iter(book_pages, page_we_want)}.\n"
      f"And it took {amount_of_times} times to find the number.")


def binary_search_recursive(array, low, high, find_x_in_array):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == find_x_in_array:
            return mid
        elif array[mid] > find_x_in_array:
            return binary_search_recursive(array, low, mid - 1, find_x_in_array)
        elif array[mid] < find_x_in_array:
            return binary_search_recursive(array, mid + 1, high, find_x_in_array)
    else:
        return -1


print(f"Recursion - "
      f"{binary_search_recursive(book_pages, 0, len(book_pages) - 1, page_we_want)}")
