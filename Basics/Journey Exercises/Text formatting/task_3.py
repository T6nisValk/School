import collections


def count_vowels(text):
    count = collections.Counter(text.lower())
    return sum(count[key] for key in count if key in "aeoiu")


print(count_vowels("aaaeeeddd"))
