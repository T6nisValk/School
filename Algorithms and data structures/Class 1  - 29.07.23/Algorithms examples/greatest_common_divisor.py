def numbers(a, b):
    while True:
        if a != b:
            if a > b:
                a = a - b
                continue
            else:
                b = b - a
                continue
        else:
            print(a)
            break


numbers(int(input("Enter num 1: ")), int(input("Enter num 2: ")))
