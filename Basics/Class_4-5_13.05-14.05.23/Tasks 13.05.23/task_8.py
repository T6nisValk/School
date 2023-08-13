# Task 8: Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73
dog_age_human_years = int(input("Enter dogs age in human years: "))
dog_age_in_dog_years = 0
for x in range(1, (dog_age_human_years + 1)):
    if x <= 2:
        dog_age_in_dog_years += 10.5
    else:
        dog_age_in_dog_years += 4

print(int(dog_age_in_dog_years))
