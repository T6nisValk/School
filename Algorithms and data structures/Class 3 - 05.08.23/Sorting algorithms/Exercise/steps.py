participants = []
valid_participants = []
with open("stepsIn.txt") as f:
    amount_of_participants = f.readline()
    keys = [
        "class", "step_length", "day_1", "day_2", "day_3", "day_4", "day_5", "day_6", "day_7"
    ]
    for line in f.readlines():
        each_line = line.strip("\n").split()

        student = {}

        for index, value in enumerate(each_line):
            student[keys[index]] = int(value)

        participants.append(student)

    for index, participant in enumerate(participants):
        if 0 not in participant.values():
            valid_participants.append(participants[index])

for some in valid_participants:
    print(some)
