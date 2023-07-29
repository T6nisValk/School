def anagrams(word, list_of_words):
    result = list(filter(lambda x: sorted(word) == sorted(x), list_of_words))
    return result


print(anagrams("abba", ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams("racer", ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams("laser", ['lazing', 'lazy', 'lacer']))
print(anagrams('listen', ['silent', 'cat', 'litens']))
