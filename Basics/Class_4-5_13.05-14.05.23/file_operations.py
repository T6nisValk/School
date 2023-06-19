# "r" - read mode (default value).
# "w" - write mode.
# "x" - creation mode. If the file already exists, the operation fails.
# "a" - appending mode.
# "b" - binary mode.
# "t" - text mode (default value).
# "+" - updating mode (read / write).

# f = open("file.txt")  # Only opens
#
# print(f.readline())
#
# f.close()  # Have to close every time

# with open("file.txt", "w") as f:  # Opens and closes the file
#     print(f)

# with open("file.txt", "r+") as f:
#    while True:
#        line = f.readline()
#        if line:
#            print(line)
#        else:
#            break

# with open("file.txt", "r") as f:
#     for line in f.readlines():
#         # If your data is only integers then int() removes new line
#         print(int(line))
#

with open("file.txt", "r") as f:
    for line in f.readlines():
        # print(line.strip(""))  # Removes given stuff from line.
        # print(line.lstrip("0\n"))  # Removes given stuff from "LEFT"
        print(line.strip("\n").rstrip("0"))  # Removes given stuff from "RIGHT"