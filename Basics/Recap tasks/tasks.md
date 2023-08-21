# Tasks for basics

>__*This is subject to update, as with every group I would think of new tasks.*__

>__*If anyone would have offers of their own: eima.blaz@gmail.com or fork enter them in and pull request them in.*__

### With topics: introduction, first program, data types, variables and operations, user input
1. Calculator to calculate area of the rectangle. area = length x width
2. This algebra monster, equation to solve a3 – b3, 
formula: (a – b)(a2 + ab + b2)
1. Area of Circle π × r2
2. Volume of the Sphere -> attached
3. This equation x2 +  y2 +  z2 – 3xyz 
formula: (x + y + z)(x2 +  y2 +  z2 – xy – yz -xz)

### With topics: text formatting, text manipulation
1. **Cats -**
Write a program that will correctly display the sentence
 "Alice has x cats"
 depending on the number of cats, it can show: Alice has 1 cat, Alice has 2 cats, Alice has 10 cats.
use user input to get amount of cats
2. **Play with words -**
Write a program that will display the given sentence every third character will be capitalized and every fourth character will have an exclamation mark after it.

    For example from
    ~~~
    Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love
    ~~~
    to
    ~~~
    CuPc!aKe !IpsUm Do!lOr !Sit amEt!. I !LovE cAr!aMel!S tOppIn!g so!UffLé I !lOve!.
    ~~~

    Try to iterate through every character in the text, by noting that the string is a list of characters.
    Test indexes of this list if it divides by 3 or 4 cleanly(no values after the dot) to get the every third and every fourth character.
    Using text generators like this: https://cupcakeipsum.com/
    Get a text and just assign it to a string variable in the program.

3. **Vowels -**
Write a program that will determine the number of vowels in a given string.
vowels = ['a', 'e', 'i', 'o', 'u']
Using text generators like this: https://cupcakeipsum.com/
Get a text and just assign it to a string variable in the program.
4. **Calculator 2.0 -**
Create a calculator that would ask user for
first number,
action,
second number,
than do the action,
display the result,
 ask user if he would like to do more actions:
 if yes, start the program again.
 if no, terminate the program.
5. **Century -**
 Introduction
 The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
 Task
 Given a year, print the century it is in.
 The year would be passed by user input
6. **BMI -**
 Write program that calculates body mass index ```(bmi = weight / (height*height))```.
 Weight(kg) and height(meters) would be passed by user input.
    ~~~
    if bmi <= 18.5 print "Underweight"
    if bmi <= 25.0 print "Normal"
    if bmi <= 30.0 print "Overweight"
    if bmi > 30 print "Obese"
    ~~~
7. **Register users -**
Write a program where when it starts user is given a couple of options
Register new user
Display users
Q for close the program
if register new user is selected ask user some basic information: name, age, city, amount of potatoes consumed yesterday.
Store that data, print thanks to user and return to main menu asking user for his action.
if Display users is selected the data about each user where every line would look like this:
    ~~~
    The participant {name}, aged {age} years old, coming from {city} have destroyed {amount_of_potatoes} potatoes yesterday.
    ~~~

### With topics: Control Instructions, Loops, Intro to functions
0.  Re-do the task Register from the last session, so that this version would be reached:
    ~~~
    if condition:
        do_this()
    elif condition:
        do_another_thing()
    elif condition:
        even_another_thing()
    else:
        break
    ~~~

1. Write a program to create a function that takes two arguments, name and age, and print their value.
2. Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.
3. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
    ~~~
    def calculation(a, b):
        # Your Code

    res = calculation(40, 10)
    print(res)
    Expected Output:
    50, 30
    ~~~
4. Using print statements form a tree in the console output. This kind of result    
    ~~~
        *
       ***
      *****
     *******
    *********
    ~~~
    
5. Write a Python program that accepts a word from the user, reverses it and prints it.
6. Write a Python program to count the number of even and odd numbers in a series of numbers
    ~~~
    Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Expected Output :
    Number of even numbers : 5
    Number of odd numbers : 4
    ~~~
7. Write a Python program that accepts a string and calculates the number of digits and letters.
    ~~~
    Sample Data : Python 3.2
    Expected Output :
    Letters 6
    Digits 2
    ~~~
8. Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
    ~~~
    Expected Output:
    Input a dog's age in human years: 15                                    
    The dog's age in dog's years is 73
    ~~~
9. Write a Python program to convert a month name to a number of days.
    ~~~
    Expected Output:
    List of months: January, February, March, April, May, June, July, August
    , September, October, November, December    

    Input the name of Month: February                                       
    No. of days: 28/29 days 
    ~~~
10. Write a program to given the time of day would return a word
Morning, Day, Evening or Night.
    ~~~
    Expected Output:
    Input time in 24 hour format: 13                                      
    Day
    ~~~
    hint: use datetime library.
    to get current time you will need to
    ~~~
    from datetime import datetime
    current_year = datetime.now().year
    ~~~

### With topics: Modules, File Operations

1. Read and Display content of the file in the most readable way you can achieve: people.txt

2. Read and Display content in the output, but sort the data based on votes received, Highest to Lowest: ```eurovision.txt```

3. Read and Display the content of it with every single character in this file shown in reverse case. Every lowercase letter should become Uppercase and every upper case should become lowercase: ```cupcake.txt```

4. Find the shortest word in the file and display it in the output together with the length of this word. ```cupcake.txt```

5. Find the average for all numbers in each line, then find the average of those average values and finally append the file with this one number in the new line: ```numbers.txt```

### With topics:  Object oriented programming

1. Design a "Rational" class representing rational numbers as pairs of integers (a numerator and a denominator).

- A class should contain many magic methods created. Functionally it should enable to:

- Display the number 0.5 in the form of ½ - the correct implementation of str and repr is required.

- The float method should return a decimal number, and int should be similar to its counterpart in the case of float numbers. Additionally, the invert method should be used.

- The comparison methods (eq, lt, gt, le, ge, cmp) should take ½ = 2/4.

- The operators +, -, *, / should be implemented correctly and return a new object of this class.

- It should be possible to save the current result to a file and load it.

- The class should always try to keep the abbreviated version of the fraction.


2. Create a class called "Car" with attributes like "make," "model," and "year."
- Create an instance of the Car class and print its attributes.
- Add a method to the Car class that calculates the car's age based on the current year.
- Create a subclass of Car called "ElectricCar" with an additional attribute for battery capacity.
- Override the Car class's method in the ElectricCar subclass to also calculate the remaining battery life.
2. Create a class called "Rectangle" with attributes for length and width.
- Add a method to the Rectangle class that calculates and returns the area.
- Create a subclass of Rectangle called "Square" that automatically sets the length and width to be equal.
- Add a method to the Square class that calculates and returns the perimeter.
3. Create a class called "Person" with attributes for name and age.
- Add a method to the Person class that prints a greeting message with the person's name.
- Create a subclass of Person called "Student" with an additional attribute for student ID.
- Override the Person class's method in the Student subclass to include the student ID in the greeting message.
4. Create a class called "BankAccount" with attributes for account number and balance.
- Add methods to the BankAccount class for depositing and withdrawing money.
- Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
- Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.