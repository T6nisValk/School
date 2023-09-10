import csv

with open("flights.csv") as data:
    destinations = {}
    airlines = {}
    lines = csv.reader(data)
    for line in lines:
        if line[2] not in destinations:
            destinations[line[2]] = 1
        else:
            destinations[line[2]] += 1

        if line[3] not in airlines:
            airlines[line[3]] = 1
        else:
            airlines[line[3]] += 1
    destinations = list(sorted(destinations.items(), key=lambda x: x[1], reverse=True))
    airlines = list(sorted(airlines.items(), key=lambda x: x[1], reverse=True))

print(
    f"Most common airline on 11 september is: {airlines[0][0]}\n"
    f"and the most common destination that day is: {destinations[0][0]}"
)
