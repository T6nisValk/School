# This part is older.
participants = []
valid_participants = []
with open("stepsIn.txt") as f:
    amount_of_participants = f.readline()
    keys = [
        "class", "step_length", "day_1", "day_2", "day_3", "day_4", "day_5", "day_6", "day_7"
    ]
    for line in f.readlines():
        each_line = line.strip("\n").split()

        participant = {}

        for index, value in enumerate(each_line):
            participant[keys[index]] = int(value)

        participants.append(participant)

    for index, participant in enumerate(participants):
        if 0 not in participant.values():
            valid_participants.append(participants[index])

    for index, participant in enumerate(valid_participants):
        valid_participants[index] = {
            "class": participant["class"],
            "steps": round((participant["step_length"] *
                           (sum([step for step in participant.values()]) -
                            participant["class"]-participant["step_length"])) / 100000, 2)
        }


# This part I did 11.08
    count = {}
    steps = {}

    for item in valid_participants:
        grade = item['class']
        steps_taken_km = item['steps']

        if grade in count:
            count[grade] += 1
            steps[grade] += steps_taken_km
        else:
            count[grade] = 1
            steps[grade] = steps_taken_km

    result = []
    for grade, count in count.items():
        result.append(
            {'class': grade, 'count': count, 'steps': steps[grade]})


with open("stepsOUT.txt", "w") as f:
    for item in result:
        f.write(f"{item['class']} {item['count']} {item['steps']}\n")
