users_list = []

with open("example_reading.txt", "w+") as f:
    f.write("example_text")

with open("example_reading.txt", "r") as f:
    keys = f.readline().strip("\n").split(" ")  # Splits the values with given value

    for line in f.readlines():
        user = line.strip("\n").split(" ")

        each_user = {}
        for index, value in enumerate(user):
            each_user[keys[index]] = value

        users_list.append(each_user)
print(users_list)
# with open("example_writing.txt", "w") as f:
#     for key in users_list[0]:
#         f.write(f"{key} ")
#     f.write("\n")
#     for user in users_list:
#         f.write(f"{user['id']} {user['name']} {user['age']} {user['city']}\n")


#  for i in users_list:
#    print(f"User {i['name']}, aged {i['age']} lives in {i['city']}.")
