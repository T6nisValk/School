# Full capital letters usually mean it has a constant value, but python still considers it as a normal variable.
# Snake case variable naming = this_is_snake_case. CamelCase = ThisIsCamelCase (usually for class naming.
# Variable names can only containt letters a-z, numbers and _. Can't start with a number.
# Assigning a value to a variable "="
number = 13
text = "Some text as a string type."
float_number = 13.923
true_false = True
print(number)
print(text)
print(float_number)
print(true_false)

# If you change the value in an already assigned variable, it changes it.
number = 31
print(f"variable number value is now {number}")

# Arithmetic operators

print(1+1)
print(2-1)
print(2*3)
print(2**3) # Power of, pow(2, 3)
print(2/2) # Float
print(4//2) # Integer
print(4%2.3) # Leftover divison. (4-2.3 = 1.7)

# Text addition
text = "Hello"
text_2 = "World"
complete_sentence = text + " " + text_2
print(complete_sentence)
complete_sentence *= 2
print(complete_sentence)

# Comparison operators, returns True or False
print(2 == 2) # Equal to
print(2 != 2) # Is not equal to
print(2 < 2) # Less than (2 <= 2) Less and equal
print(2 > 2) # More than (2 >= 2) More and equal

# Assignment operators
number = 3
print(number)
number += 3
print(number)
number -= 3
print(number)
number *= 3
print(number)
number **= 3
print(number)
number /= 3
print(number)
number //= 3
print(number)

# Indentity operator
number = 1
print(number is number) # Checks if the value and type are the same
print(number is not number) # Checks if the value and type are not the same

# Logical operators and / or / not
		# True and True == True
		# True and False == False
		# False and False == False

		# True or True == True
		# True or False == True
		# False or False == False
num_1 = 1
num_2 = 2
print(num_1 is num_2 and num_1 is num_2)

# Membership operators in / not in
text = "Cool"
print("f" in text)
print("f" not in text)



