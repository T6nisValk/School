import re

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-',
              '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': "SOS"}


def decode_morse(morse):
    # Remove spaces from sides
    morse.strip()
    # Split words into a list
    list_of_morse_words = re.split(r"\s{2}", morse)
    # Split words into letters
    list_of_morse_word_letters = [word.split() for word in list_of_morse_words]
    # Convert morse to letters
    list_of_word_letters = [["".join([MORSE_CODE.get(s) for s in word])] for word in
                            list_of_morse_word_letters]
    # Get the letters from list of word letters
    result = []
    for list_ in list_of_word_letters:
        for word in list_:
            result.append(f" {word}")
    # Join the letters and then the words, remove leading space
    result = "".join(result).lstrip()
    return result


print(decode_morse('.... . -.--   .--- ..- -.. .'))
print(decode_morse(' . '))
print(decode_morse('...   ---   ...'))
