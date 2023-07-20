def weird_text(text):
    result = []
    for index, word in enumerate(text.split()):
        if index % 2 == 0:
            result.append(word.capitalize())
        elif index % 3 == 0:
            result.append(word + "!")
        else:
            result.append(word)
    return " ".join(result)


print(weird_text("Hello my dear little world, why are you so weird looking?"))
