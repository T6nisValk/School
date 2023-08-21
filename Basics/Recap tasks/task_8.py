"""
Write a program that will determine the number of vowels in a given string. 
vowels = ['a', 'e', 'i', 'o', 'u']
"""


def count_vowels(text):
    return sum([text.count(vowel) for vowel in "aeiou"])
