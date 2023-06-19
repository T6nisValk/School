animals = ["Cat", "Dog", "Bear", "Horse", "Elephant"]

x = 10
y = 1

# while True:
#     user_input = input("Enter something(Q to quit): ")
#
#     if user_input == "Q":
#         break
#     elif user_input == "a":
#         a = 5 + 5
#         if a != 10:
#             continue
#         print("potatoe")
#     else:
#         print("Your input didn't do anything.")

while y <= x:
    print(y)
    y += 1

while "Cat" in animals:
    print("Cat is in the list.")
    break

for animal in animals:
    print(f"{animal} is in index {animals.index(animal)}")



x = 0
while x < len(animals):
    print(animals[x])
    x += 1

numbers = []
numbers_1 = []
number = 1
while number <= 100:
    numbers.append(number)
    number += 1
print(numbers)


# range(x) = 0 - x
# range(y, x) = y - x
# range(y, x, z) = y - x, with a step of z
for num in range(1, 101, 3):
    numbers_1.append(num)
print(numbers_1)