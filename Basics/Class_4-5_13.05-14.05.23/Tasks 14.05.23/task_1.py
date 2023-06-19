# Read and Display content of the file in the most readable way you can achieve: people.txt
with open("people.txt") as f:
    headers = f.readline().strip("\n").split(",")
    for line in f.readlines():
        people = line.strip("\n").split(",")
        print(f"{people[1]} {people[2]}, email: {people[3]}, gender: {people[4]}")
