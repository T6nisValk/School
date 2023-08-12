with open("source.txt") as source:
    amount_of_tasks = int(source.readline())
    amount_of_time_each_task = source.readline().strip().split()
    amount_of_points_each_task = source.readline().strip().split()
    participants = []
    participant_points = []
    result = []
    for participant in source.readlines():
        person = {}
        total_time = 0
        total_points = 0
        completed_tasks = 0
        for index, value in enumerate(participant.strip().split()[1:]):
            total_time += int(value)
            time = int(amount_of_time_each_task[index])
            point = int(amount_of_points_each_task[index])
            if int(value) == 0:
                total_points += 0
            else:
                completed_tasks += 1
                if 0 < int(value) <= time:
                    total_points += point
                elif time < int(value):
                    total_points += point//2
        participant_points.append(total_points)
        person["name"] = participant.split()[0]
        person["completed tasks"] = completed_tasks
        person["total task time"] = total_time
        person["total points"] = total_points
        result.append(person)

        for index, contestant in enumerate(result):
            if contestant["total points"] < max(participant_points):
                result.remove(contestant)

        sorted_result = sorted(
            result, key=lambda x: x["completed tasks"], reverse=True)

with open("result.txt", "w") as f:
    f.write(f"{str(max(participant_points))}\n")
    for line in sorted_result:
        f.write(
            f"{line['name']} {line['completed tasks']} {line['total task time']}\n")
