import re

filename = "Intermediate\Class 5 - 09.07.23\Exercises\\text.txt"
with open(filename) as f:
    data = f.read()

pattern = r"@[a-zA-Z0-9]+"
result = re.findall(pattern, data)
print(result)
