# Find the city and the county that grew the most by % compared between 2014 and 2018.


with open("towns.txt") as f:
    # Clean up data
    header = f.readline().strip().split(",")
    data = []
    for line in f.readlines():
        town = {}
        for index, value in enumerate(line.strip().split(",")):
            if index != 0:
                town[header[index]] = value
        data.append(town)

    # Filter out towns that didn't grow in population.
    towns_that_grew = []
    for town in data:
        if int(town["Population 2014"]) < int(town["Population 2018"]):
            towns_that_grew.append(town)

    # Find the growth percentage.
    towns_that_grew_with_percentage = []
    for town in towns_that_grew:
        difference = int(town["Population 2018"]) - int(town["Population 2014"])
        percentage = (difference * 100) / int(town["Population 2014"])
        town["Growth"] = round(percentage, 2)
        towns_that_grew_with_percentage.append(town)

    # Find the highest growth town.
    towns_that_grew_with_percentage = sorted(
        towns_that_grew_with_percentage, key=lambda x: x["Growth"], reverse=True
    )
    highest_growth_town = towns_that_grew_with_percentage[0]["Town"]
    highest_growth_town_percentage = towns_that_grew_with_percentage[0]["Growth"]

    # Find the highest growth county.
    county_growth = {}
    for town in towns_that_grew_with_percentage:
        if town["County"] in county_growth:
            county_growth[town["County"]] += town["Growth"]
        else:
            county_growth[town["County"]] = town["Growth"]

    # Sort counties by growth percentage.
    county_growth = list(
        sorted(county_growth.items(), key=lambda x: x[1], reverse=True)
    )
    highest_growth_county = county_growth[0][0]
    highest_growth_county_percentage = county_growth[0][1]

# Result
print("-" * 120)
print(
    f"Highest population growth from 2014 to 2018 was in town "
    f"{highest_growth_town}, "
    f"with a growth percentage of "
    f"{highest_growth_town_percentage}%."
)
print(
    f"Highest population growth from 2014 to 2018 was in county "
    f"{highest_growth_county}, "
    f"with a growth percentage of "
    f"{highest_growth_county_percentage}%."
)
print("-" * 120)
