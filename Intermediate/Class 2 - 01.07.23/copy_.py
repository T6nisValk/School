from copy import deepcopy
from dataclass import Book

book1 = Book("Try again", "Value", 2021)
original_list = ["Apple", "Pear", book1]

shallow_copy = list(original_list)
deepcopy_ = deepcopy(original_list)

original_list[0] = "Plum"
book1.name = "new name"
print(original_list[2].name)
print(shallow_copy[2].name)  # Modifying the original also affects the copy.
print(deepcopy_[2].name)  # Modifying the original does not affect the copy.
