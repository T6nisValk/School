# Task 10: Write a program to given the time of day would return a word
# Morning, Day, Evening or Night
# hint: use datetime library.
# to get current time you will need to
# from datetime import datetime
#
# current_time = datetime.now().time()

from datetime import datetime
current_time = datetime.now().time()

if int(current_time.strftime("%H%M%S")) in range(60000, 115959):
    print("It's morning.")
elif int(current_time.strftime("%H%M%S")) in range(120000, 155959):
    print("It's day.")
elif int(current_time.strftime("%H%M%S")) in range(160000, 205959):
    print("It's evening.")
elif int(current_time.strftime("%H%M%S")) in range(1, 55959):
    print("It's night.")
elif int(current_time.strftime("%H%M%S")) in range(210000, 235959):
    print("It's night.")


