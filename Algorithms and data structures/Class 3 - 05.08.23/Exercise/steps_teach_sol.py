def process_data(participants):
    result = []
    for participant in participants:
        all_steps = 0
        for steps in participant[2:]:
            all_steps += int(steps)
        kilometers = round((int(participant[1]) * all_steps) / 100000, 2)
        if not len(result):
            result.append(
                {"grade": participant[0], "amount": 1, "kilometers": kilometers}
            )
        else:
            is_new = True

            for index, record in enumerate(result):
                if record["grade"] == participant[0]:
                    is_new = False
                    result[index] = {
                        "grade": record["grade"],
                        "amount": record["amount"] + 1,
                        "kilometers": record["kilometers"] + round(kilometers, 2),
                    }

            if is_new:
                result.append(
                    {
                        "grade": participant[0],
                        "amount": 1,
                        "kilometers": round(kilometers, 2),
                    }
                )

    return result


with open("stepsIn.txt") as source:
    amount_of_participants = int(source.readline())

    participants = []
    for _ in range(amount_of_participants):
        is_participating = True

        participant = source.readline().strip().split()
        steps_sum = 0
        for steps in participant[2:]:
            if steps == "0":
                is_participating = False
        if is_participating:
            participants.append(participant)

with open("stepsOUT.txt", "w") as output:
    for line in process_data(participants):
        output.write(f"{line['grade']} {line['amount']} {line['kilometers']}\n")
