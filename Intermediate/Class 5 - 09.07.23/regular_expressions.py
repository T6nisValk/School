import re

text = "I love python. Python is a powerful language"

# re.match (pattern, string)
match_result = re.match(r"Python", text)

if match_result:
    print("Match was found.")
else:
    print("Match was not found.")

# re.search (pattern, string)
match_result = re.search(r"Python", text)

if match_result:
    print("Match was found.")
else:
    print("Match was not found.")

# re.findall (pattern, string)
# \b word boundary. Start to end. r"\b\w{6}\b" - any 6 letter word.
match_result = re.findall(r"\b\w{6}\b", text)  # Returns a list of matched patterns.
print(match_result)

# re.split (pattern, string)

match_result = re.split(r"\s", text)
print(match_result)

# re.sub (pattern, replace, string, count(default unlimited))
match_result = re.sub(r"\b\w{6}\b", ".NET", text, count=1)
print(text)
print(match_result)

# re.subn (pattern, replace, string, count(default unlimited))
match_result = re.subn(r"\b\w{6}\b", ".NET", text)
print(text)
print(match_result)  # Tuple, with the string and count.
