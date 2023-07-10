import re

"""
Task 1
"""


def get_unique_level():
    filename = "logs.txt"
    data = []
    with open(filename) as logs:
        for line in logs:
            if re.search(r"^[0-9/]{5}", line):
                data.append(
                    " ".join(" ".join(line.strip().split()[2::]).split(":")[:1:]).strip(" "))
    unique_levels = []
    for line in data:
        if line not in unique_levels:
            unique_levels.append(line)

    return unique_levels


print(f"Unique messages: {get_unique_level()}")

"""
Task 2
"""


def errors_per_day():
    filename = "logs.txt"
    dates = []
    with open(filename) as logs:
        for line in logs:
            if re.search(r"^[0-9/]{5}", line):
                dates.append(line.strip().split(" ")[0])
    unique_dates = []
    for date in dates:
        if date not in unique_dates:
            unique_dates.append(date)
    data = {}
    for unique_date in unique_dates:
        data[unique_date] = dates.count(unique_date)
    return data


print(f"Errors per date: {errors_per_day()}")
