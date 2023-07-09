import re

filename = "text.txt"
with open(filename) as f:
    data = f.read()

pattern = r"@[a-zA-Z0-9]+"
result = re.findall(pattern, data)
print(result)
