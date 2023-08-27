import time


with open("data.txt") as data:
    print("Reading data...")
    time.sleep(1)
    some_data_from_file = []
    for line in data.readlines():
        some_data_from_file.append(line.strip("\n"))
    time.sleep(1)
    print("Reading data complete.")

filename_write = input("Enter the name for the file to write the data to: ")
print("Writing data...")
time.sleep(1)
with open(f"{filename_write}.txt", "w") as output:
    for data in some_data_from_file:
        output.write(f"{data}\n")
time.sleep(1)
print("Writing data complete.")
