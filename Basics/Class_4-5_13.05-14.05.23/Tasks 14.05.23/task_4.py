# Find the shortest word in the file and display it in the output together with the length of this word. cupcake.txt
with open("Basics\Class_4-5_13.05-14.05.23\Tasks 14.05.23\cupcake.txt") as f:
    words_dict = {}
    words_import = f.read().split(" ")
    for word in words_import:
        words_dict[word] = len(word)
word_length = 100  # Base value
word = ""
for key, value in words_dict.items():
    if value < word_length:
        word_length = value
        word = key

print(word, word_length)
