# with open("example_writing.txt", "a") as f:
#
#     f.write("tõnis \n")


with open('example_writing.txt', "w") as f:
    for user in users:
        f.write(user)
