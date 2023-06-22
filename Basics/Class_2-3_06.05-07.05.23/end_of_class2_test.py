# Task 1: Cats
# Write a program that will correctly display the sentence
#  "Alice has x cats"
#  depending on the number of cats, it can show: Alice has 1 cat, Alice has 2 cats, Alice has 10 cats.
# use user input to get amount of cats

number_of_cats = int(input("How many cats does Alice have?: "))
if number_of_cats > 1:
    print(f"Alice has {number_of_cats} cats.")
else:
    print(f"Alice has {number_of_cats} cat.")


# Task 2: Play with words
# Write a program that will display the given sentence.
# Every third character will be capitalized and every fourth character will have an exclamation mark after it.
# Using text generators like this: https://cupcakeipsum.com/
# Get a text and just assign it to a string variable in the program.

random_text = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love"
# Enumerate lists the index and value of list
for index, char in enumerate(random_text):
    if (index + 1) % 3 == 0:
        print(char.upper(), end="")
    elif (index + 1) % 4 == 0:
        print(f"{char}!", end="")
    else:
        print({char}, end="")

# Task 3: Vowels
# Write a program that will determine the number of vowels in a given string.
# vowels = ['a', 'e', 'i', 'o', 'u']
# Using text generators like this: https://cupcakeipsum.com/
# Get a text and just assign it to a string variable in the program.

random_text = input("Enter you text here to count the vowels in it: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for vowel in vowels:
    vowel_count += random_text.count(vowel)
print(f"There are {vowel_count} vowels in your sentence.")


# Task 4: Calculator 2.0
# Create a calculator that would ask user for
# first number,
# action,
# second number,
# than do the action,
# display the result,
#  ask user if he would like to do more actions:
#  if yes, start the program again.
#  if no, terminate the program.

while True:
    try:
        num_1 = int(input("Enter the first number: "))
        op_1 = input("Enter the operator: ")
        num_2 = int(input("Enter the second number: "))
    except ValueError:
        print("Not a number")
        continue

    if op_1 == "/":
        print(f"Your answer is {num_1 / num_2}.")
    elif op_1 == "*":
        print(f"Your answer is {num_1 * num_2}.")
    elif op_1 == "+":
        print(f"Your answer is {num_1 + num_2}.")
    else:
        print(f"Your answer is {num_1 - num_2}.")
    user_input = input("Do you want to do a different calculation?(Yes/No): ")
    if user_input.upper() == "YES":
        continue
    else:
        print("Good bye.")
        break


# Task 5. Century Introduction The first century spans from the year 1 up to and including the year 100, the second
# century - from the year 101 up to and including the year 200, etc. Task Given a year, print the century it is in.
# The year would be passed by user input

user_input = int(input("Enter the year: "))
if user_input < 0:
    print("Not a valid year.")
elif user_input <= 100:
    print("1st century")
elif user_input % 100 == 0:
    print(user_input // 100, "century")
else:
    print(user_input // 100 + 1, "century")

# Task 6. BMI
#  Write program that calculates body mass index (bmi = weight / height**2).
#  Weight and height would be passed by user input.
# if bmi <= 18.5 print "Underweight"
# if bmi <= 25.0 print "Normal"
# if bmi <= 30.0 print "Overweight"
# if bmi > 30 print "Obese"

user_weight = int(input("Enter your weight(kg): "))
user_height = float(input("Enter your height(m): "))
bmi = round(user_weight / user_height ** 2, 2)
if bmi <= 18.5:
    print(f"You are underweight with a bmi of {bmi}")
elif bmi <= 25.0:
    print(f"You are at a normal weight with a bmi of {bmi}")
elif bmi <= 30.0:
    print(f"You are overweight with a bmi of {bmi}")
elif bmi > 30:
    print(f"You are obese with a bmi of {bmi}")

# Task 7.  Register users Write a program where when it starts user is given a couple of options Register new user
# Display users if register new user is selected ask user some basic information: name, age, city, amount of potatoes
# consumed yesterday. Store that data, print thanks to user and return to main menu asking user for his action. if
# Display users is selected the data about each user where every line would look like this: The participant {name},
# aged {age} years old, coming from {city} have destroyed {amount_of_potatoes} potatoes yesterday.

user = {}

while True:

    user_input = input("What would you like to do?\n"
                       "To register a new user, enter REGISTER,\n"
                       "To display current user, enter DISPLAY.\n"
                       "To quit the program, enter QUIT. \n")
    if user_input.upper() == "REGISTER":
        user["name"] = input("Enter your name: ")
        user["age"] = int(input("Enter your age: "))
        user["city"] = input("Enter your city: ")
        user["amount_of_potatoes"] = input(
            "How may potatoes did you eat yesterday?: ")
        print("Thanks for registering!")
        continue
    elif user_input.upper() == "DISPLAY":
        print(f"The participant {user.get('name')},"
              f" aged {user.get('age')} years old,"
              f" coming from {user.get('city')} have destroyed {user.get('amount_of_potatoes')} potatoes yesterday.")
    elif user_input.upper() == "QUIT":
        break
    else:
        print("Not a correct input, try again.")
        continue
