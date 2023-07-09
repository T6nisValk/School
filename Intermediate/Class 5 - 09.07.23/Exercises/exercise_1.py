import gzip
import re

filename = "aspell_en_CA.txt.gz"
pattern = r"\b[a-zA-Z]{3}\b"
with gzip.open(filename, mode="rt") as f:
    for word in f:
        if re.search(pattern, word):
            print(word.strip())

# result = re.findall(pattern, data)
# print(result)
