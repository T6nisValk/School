def odd_indexes(string):
    if type(string) == "str":
        return string[1::2]
    else:
        return str(string)[1::2]
