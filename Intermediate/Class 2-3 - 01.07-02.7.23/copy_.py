from copy import deepcopy, copy
from dataclass import Book
book1 = Book("Try again", "Value", 2021)
original_list = ["Apple", "Pear", book1]

shallow_copy = list(original_list)
deepcopy_ = deepcopy(original_list)

original_list[0] = "Plum"
book1.name = "new name"
print(original_list[2].name)
print(shallow_copy[2].name)  # Does not keep the original data.
print(deepcopy_[2].name)  # Keeps the original data as a copy.
