# Read and Display the content of it with every single character in this file shown in reverse case.
# Every lowercase letter should become Uppercase and every upper case should become lowercase: cupcake.txt
with open("cupcake.txt") as f:
    for character in f.read():
        if character.isupper():
            print(f"{character.lower()}", end="")
        else:
            print(f"{character.upper()}", end="")
