# Task 9: Write a Python program to convert a month name to a number of days.
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days

year = {
    "January": "31",
    "February": "28/29",
    "March": "31",
    "April": "30",
    "May": "31",
    "June": "30",
    "July": "31",
    "August": "31",
    "September": "30",
    "October": "31",
    "November": "30",
    "December": "31",
}

print(
    "List of months: January,"
    " February, March, April,"
    " May, June, July, August,"
    " September, October, November, December"
)
user_input = input("Enter the name of Month: ")

for key, value in year.items():
    if user_input.upper() == key.upper():
        print(f"No. of days in given month is: {value}")
        break
    else:
        continue
