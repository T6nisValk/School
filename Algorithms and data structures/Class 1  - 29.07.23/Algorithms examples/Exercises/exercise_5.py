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
    morse_words = morse.split("  ")
    # Split words into letters
    morse_letters = [word.split() for word in morse_words]
    # Convert morse to letters
    alpha_letters = [["".join([MORSE_CODE.get(s) for s in word])] for word in
                     morse_letters]
    # Get the letters from list of word letters
    result = "".join(
        ["".join([f" {word}" for word in list_]) for list_ in alpha_letters]).lstrip()
    return result


print(decode_morse('.... . -.--   .--- ..- -.. .'))
print(decode_morse(' . '))
print(decode_morse('...   ---   ...'))
