# Create a user class
# initialize the fields of the user: id, name, age, city, potato
# create two methods:
#    register_user( id, name, age, city, potato):
#        responsible for returning formed user data.
#        collecting the data from userInput and storing it in the users list is not included to this method
# display_user:
# print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
#              f"destroyed {self.potato} potatoes yesterday.")
# Adjust the code, so it would still work after these adjustments.

class User:
    def __init__(self, id, name, age, city, potato):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.potato = potato

    def register_user(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.city = input("Enter your city: ")
        self.potato = input("Enter your potato: ")

        last_user = users[len(users) - 1]
        users.append({'id': int(last_user['id']) + 1, 'name': self.name, 'age': self.age, 'city': self.city,
                      'potato': self.potato})

    def display_user(self):
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
              f"destroyed {self.potato} potatoes yesterday.")


def get_users_from_file():
    users_list = []
    with open("example.txt") as f:
        headers = f.readline().strip('\n').split(" ")
        for line in f.readlines():
            user = line.strip().split(" ")
            each_user = {}
            for index, value in enumerate(user):
                each_user[headers[index]] = user[index]
            users_list.append(each_user)
    return users_list


def save_users_to_file():
    with open('example.txt', 'w+') as f:
        for key in users[0]:
            f.write(f"{key} ")
        f.write("\n")
        for user in users:
            f.write(
                f"{user['id']} {user['name']} {user['age']} {user['city']} {user['potato']}\n")
    print("Your users were saved successfully")


print("Hello what would you like to do?")
users = get_users_from_file()

while True:
    primary_action = input("1. Register new user \n"
                           "2. Display users \n"
                           "3. for close the program\n"
                           "Your choice: ")

    if primary_action == '1':
        user = User(users[len(users) - 1]['id'] + str(1),
                    users[len(users) - 1]['name'],
                    users[len(users) - 1]['age'],
                    users[len(users) - 1]['city'],
                    users[len(users) - 1]['potato'])
        user.register_user()
        save_users_to_file()


    elif primary_action == '2':
        for user in users:
            user.display_user()

    elif primary_action == '3':
        save_users_to_file()
        break
    else:
        print("Something does not seem to add up.. please read the menu options :) ")
