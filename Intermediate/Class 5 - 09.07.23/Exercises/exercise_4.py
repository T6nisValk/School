import re

filename = "text.txt"
with open(filename) as f:
    data = f.read()
result = re.findall(r"@[a-zA-Z0-9]+", data)
print(result)
