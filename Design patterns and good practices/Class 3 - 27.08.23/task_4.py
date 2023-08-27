def reverse_sentence(text):
    return " ".join(text.rstrip(".").split()[::-1]).capitalize()


text = "This is a sample sentence."

print(f"Sentence to be reverse:\n{text}")
print(f"Reversed sentence:\n{reverse_sentence(text)}.")
