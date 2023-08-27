# Topic: Serialization Task: Build a program that stores
# a dictionary of user information (name, age, email) in a JSON file.
# Allow the user to add or update information. Implement serialization
# and deserialization for reading and writing the JSON file.

import json


def create_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user = {name: {"age": age, "email": email}}
    try:
        with open("data.json") as f:
            data = json.load(f)
        data.update(user)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as f:
            json.dump(user, f, indent=2)


def show_users():
    try:
        with open("data.json") as f:
            print("-" * 25)
            data = json.load(f)
            if not data:
                print("No users.")
            else:
                for user in data:
                    print(f"{user}: {data[user]}")
    except json.decoder.JSONDecodeError:
        print("No users.")


def edit_user():
    print("-" * 25)
    print("Which user would you like to edit?")
    user_input_name = input("Enter name: ")
    print("What would you like to change?")
    user_input = input("Enter: ")
    print("What would you like to change it to?")
    user_new_value = input("Enter: ")

    with open("data.json") as f:
        data = json.load(f)
        for value in data:
            if user_input_name == value:
                if user_input == "age":
                    data[value][user_input] = user_new_value
                elif user_input == "email":
                    data[value][user_input] = user_new_value
                elif user_input == "name":
                    new_user = data[value]
                    data.pop(value)
                    data[user_new_value] = new_user
                break

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    print("User updated.")


def remove_user():
    print("Which user you would like to remove?")
    user_input = input("Enter name: ")
    with open("data.json") as f:
        data = json.load(f)
        data.pop(user_input)
    with open("data.json", "w") as f:
        json.dump(data, f)


while True:
    print("-" * 25)
    print(
        "What would you like to do?\n"
        "To show users - 1\n"
        "To create a user - 2\n"
        "To edit a user - 3\n"
        "To remove a user - 4\n"
        "To exit program - 5"
    )
    print("-" * 25)
    user_input = int(input("Enter: "))

    if user_input == 1:
        show_users()

    elif user_input == 2:
        create_user()

    elif user_input == 3:
        edit_user()

    elif user_input == 4:
        remove_user()

    elif user_input == 5:
        exit()
