import csv

filename = 'student.csv'
# Read from .CSV
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row.
    for datarow in reader:
        print(datarow)

# Write to an existing .CSV
# -r, -w, -a
with open(filename, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Jadon Sancho", "B444", "Unemployed"])

# Create and write to a .CSV
record = [
    ["Item", "Quantity", "Cost"],  # Header
    ["Apple", 10, 12.30],
    ["Spinach", 1, 2.30],
    ["Black plums", 10, 4.99]
]
filename = "groceries_a.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    for row in record:
        writer.writerow(row)
filename = "groceries_b.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(record)  # Any iterable
