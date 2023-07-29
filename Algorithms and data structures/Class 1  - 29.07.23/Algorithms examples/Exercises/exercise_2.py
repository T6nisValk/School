def anagrams(word, list_of_words):
    result = list(filter(lambda x: sorted(word) == sorted(x), list_of_words))
    print(result)


anagrams("abba", ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams("racer", ['crazer', 'carer', 'racar', 'caers', 'racer'])
anagrams("laser", ['lazing', 'lazy', 'lacer'])
