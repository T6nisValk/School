# Read and Display content of the file in the most readable way you can achieve: people.txt
with open("Basics\Class_4-5_13.05-14.05.23\Tasks 14.05.23\people.txt") as f:
    headers = f.readline().strip("\n").split(",")
    for line in f.readlines():
        people = line.strip("\n").split(",")
        print(
            f"{people[1]} {people[2]}, email: {people[3]}, gender: {people[4]}")
