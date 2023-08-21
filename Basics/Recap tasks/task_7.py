"""
Play with words - 
Write a program that will display the given sentence 
every third character will be capitalized 
and every fourth character will have an exclamation mark after it.
"""


def text_manipulation(text):
    new_text = ""
    for index, letter in enumerate(text):
        if index % 2 == 0:
            new_text += letter.upper()
        elif index % 3 == 0:
            new_text += f"{letter}!"
        else:
            new_text += letter

    return new_text
