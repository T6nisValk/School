import re

print("-" * 100)
"""
Example 1: Match a single character between c and t.
"""
print("Example 1: find 'cat'.")
string1 = "The cat sat on the ledge of Mr. Catdoso's fence."
print(string1)
pattern1 = r"[c|C].[t|T]"
match_result1 = re.findall(pattern1, string1)  # c or C . t or T
print(match_result1)
print("-" * 100)

print("Example 2: Starts/ends with.")
"""
^ = start
$ = end

Example 2: Check if a string begins with a word.
"""
string2 = "Hello my dear world, why are you so mean?"
print(string2)
# Can also use re.match check if starts with.
pattern2 = r"^Hello"
match_result2 = re.search(pattern2, string2)
if match_result2:
    print(f"Starts with 'Hello'.")
else:
    print(f"Doesn't start with 'Hello'")
pattern2_2 = r"mean$"
match_result2 = re.search(pattern2_2, string2)
if match_result2:
    print(f"Ends with 'mean'.")
else:
    print(f"Doesn't end with 'mean'")
print("-" * 100)

"""
Example 3: Return one or more digits.
"""

string3 = "I bought apples for 9.47, bread for 55.62 and chicken for 12.89. I am left with " \
          "$20.00. I can loan you $5."
print("Example 3: Return digit(s).")
print(string3)
pattern3 = r"\d+.\d+|\d+"
match_result3 = re.findall(pattern3, string3)  # \d+(.\d+)*
print(f"All digits in string are: {match_result3}")
print("-" * 100)

"""
Example 4: Extract hexadecimal colors.
"""

print("Example 4: Find hexadecimal color code.")
string4 = "#A49693, #541A0D, #25201F are hexa colors. 482738 is not a hexa color. " \
          "#FFF is also an hexadecimal color."
print(string4)
pattern4 = r"#[0-9a-fA-F]{3,6}"
match_result4 = re.findall(pattern4, string4)
print(f"Hexadecimal color codes in this string is/are: {match_result4}")
print("-" * 100)

"""
Example 5: Find email addresses.
"""
print("Example 5: Find emails in string.")
string5 = "These are emails:\n" \
          "example@gmail.com\n" \
          "example@yahoo.co.uk\n" \
          "test@email.gov\n" \
          "ad.test@seeme.info\n" \
          "@someaddress.com"
print(string5)
pattern5 = r"\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[.A-Z|a-z]{2,}\b"
match_result5 = re.findall(
    pattern5, string5)
print(f"Valid emails in string: {match_result5}.")
print("-" * 100)

"""
Example 6: Find valid date.
"""
print("Example 6: Find valid date.")
string6 = "Dates:\n" \
          "2023-07-09\n" \
          "July 07, 2023\n" \
          "Dates 2022/07/09\n" \
          "20220709"
print(string6)
pattern6 = r"\b\d{4}[-|/]\d{2}[-|/]\d{2}\b"
match_result6 = re.findall(pattern6, string6)
print(f"Valid dates in string: {match_result6}.")
print("-" * 100)

"""
Example 7: Validating a strong password.
- Minimum of 8 characters
- At least 1 uppercase
- At least one digit
- At least one special character.
"""
print("Example 7: Strong password.")
passwords = ["P@ssw0rd", "P@sssw0rd", "password", "Password!123"]
print(passwords)
pattern7 = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\d)(?=.*[!@#%^*|])[A-Za-z\d$@_\-.#!%&]{8,}$"
match_result8 = [password for password in passwords if re.findall(
    pattern7, password)]
print(f"Strong passwords are: {match_result8}.")
