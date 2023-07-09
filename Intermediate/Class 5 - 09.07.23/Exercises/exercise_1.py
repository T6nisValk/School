import gzip
import re

filename = "aspell_en_CA.txt.gz"
with gzip.open(filename, mode="rt") as f:
    for word in f:
        if re.search(r"\b[a-zA-Z]{3}\b", word):
            print(word.strip())

# result = re.findall(pattern, data)
# print(result)
