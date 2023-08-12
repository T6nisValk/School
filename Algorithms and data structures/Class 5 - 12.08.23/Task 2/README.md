# Password check

Write a program to say if my entered passwords are strong or weak based on the data I have about previous passwords.

Similarity between passwords is calculated based on passwords parameters difference absolute sum. E.g. when comparing Katinas.33#? and Pyragaitis12! you would need to:

```
12-13 = -1 > absolute value 1
1-1 = 0
6-9 = -3 > absolute value 3
2-2 = 0
3-1 = 2 > absolute value 2

Sum of absolute values = 6, thus similarity index between these passwords is 6.

You will get the srength of the password based on with witch password of the sample there will be lowest similarity index with.
```



Source file:
````
2 7
Katinas.33#? 12 1 6 2 3
kasa11 6 0 4 2 0
slaptas135 10 0 7 3 0 mid
admin 5 0 5 0 0 week
Pyragaitis12! 13 1 9 2 1 strong
11Auto11 8 1 3 4 0 mid
abcdef1 7 0 6 1 0 week
<EgZaMiNaS> 11 5 4 0 2 strong
saitas1 7 0 6 1 0 week
``````
1. First value is amount of password I enter to check, Second value is the amount of passwords there are for sample
2. First two passwords are the ones I want to check, their structure is:
- Password
- Password length
- Amount of capital letters
- Amount of lowercase letters
- Amount of digits
- Amount of special characters
3. Other 7 lines is the sample data and their structure is:
- Password
- Password length
- Amount of capital letters
- Amount of lowercase letters
- Amount of digits
- Amount of special characters
- Strength:[weak, mid, strong]

Result should be:
````
Katinas.33#? strong 6
Pyragaitis12!
kasa11 week 4
abcdef1
saitas1
admin
``````
Explanation:

Showing password I want to check, Strength, the difference index with the closest password. List of passwords that matched the same similarity with the provided password.