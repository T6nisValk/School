import re

list_of_something = ["goal", "new", "user", "sit", "eat", "dinner"]
print([val for val in list_of_something if re.search(r"[aw]", val)])
