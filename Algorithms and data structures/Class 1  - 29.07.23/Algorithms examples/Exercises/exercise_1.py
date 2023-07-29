def likes(names):
    if len(names) == 1:
        print(f"{names[0]} likes it!")
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]} like it!")
    elif len(names) == 3:
        print(f"{names[0]}, {names[1]} and {names[2]} like it!")
    elif len(names) > 3:
        print(f"{names[0]}, {names[1]} and {len(names) - 2} other people like it!")
    else:
        print("Nobody likes it..")
    pass


likes([])
likes(["Peter"])
likes(["Peter", "Anna"])
likes(["Peter", "Anna", "Mark"])
likes(["Peter", "Anna", "Mark", "Ola"])
