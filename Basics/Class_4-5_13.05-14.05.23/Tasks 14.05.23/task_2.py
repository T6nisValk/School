# Read and Display content in the output, but sort the data based on votes received, Highest to Lowest: eurovision.txt
contestants_list = []
with open("eurovision2019.txt") as f:
    headers = f.readline().strip("\n").split(",")
    for line in f.readlines():
        contestant = line.strip("\n").split(",")
        contestants = {}
        for index, value in enumerate(contestant):
            contestants[headers[index]] = value
        contestants_list.append(contestants)

sorted_contestants_list = sorted(contestants_list, key=lambda votes: votes["Jury Votes"], reverse=True)
print(f"\033[1;32m Contestants in order by Jury Votes, highest to lowest:")
for each_contestant in sorted_contestants_list:
    print(f"\033[1;31m {each_contestant['Country']} - {each_contestant['Artist']} - "
          f"{each_contestant['Song']} - {each_contestant['Jury Votes']}")
