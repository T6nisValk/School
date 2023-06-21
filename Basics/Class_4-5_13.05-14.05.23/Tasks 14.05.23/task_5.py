# Find the average for all numbers in each line,
# then find the average of those average values
# and finally append the file with this one number in the new line: numbers.txt
# ----------------------------------------------------------------------------------- #
# Empty lists.
from statistics import mean
list_of_lines = []
list_of_line_averages = []
with open("Basics\Class_4-5_13.05-14.05.23\Tasks 14.05.23\numbers.txt") as f:
    for lines in f.readlines():
        # Line check to run the program again, skips lines that are already appended.
        if lines.startswith("Average"):
            continue
        elif lines.startswith(" "):
            continue
        elif lines.startswith("\n"):
            continue
        # Create a list of lines.
        list_of_lines.append(lines.strip("\n").split("  "))
    for line in list_of_lines:
        # Iterate through each value in line lists and convert to int.
        for index, value in enumerate(line):
            line[index] = int(value)
        # Create a list of line averages using sum() of list items /len().
        list_of_line_averages.append(mean(line))
    # Get average of line averages with sum() of list items/len().
    result = round(mean(list_of_line_averages), 3)
# Append result
with open("numbers.txt", "a") as f:
    f.write(f"\nAverage of all: {str(result)}")
# ----------------------------------------------------------------------------------- #
