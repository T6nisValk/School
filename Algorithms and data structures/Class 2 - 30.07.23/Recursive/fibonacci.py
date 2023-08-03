import time


def fibbo(len_of_times):
    times = range(len_of_times)
    result = []
    for index in times:
        if index == times[0]:
            result.append(0)
        elif index == times[1]:
            result.append(1)
        else:
            result.append(result[index - 1] + result[index - 2])
    return result[-1]


# for n in range(1, 50):
#     print(f"{n}: {fibbo(n)}")


def fibbo_recursive(len_of_times, memory={}):
    if len_of_times == 1:
        return 1
    elif len_of_times == 2:
        return 1
    elif len_of_times > 2:
        if len_of_times in memory:
            return memory[len_of_times]
        memory[len_of_times] = fibbo_recursive(len_of_times - 1) + fibbo_recursive(len_of_times - 2)
        return memory[len_of_times]


for n in range(1, 50):
    start = time.perf_counter()
    print(f"{n}: {fibbo_recursive(n)}")
    finish = time.perf_counter()
    print(finish - start)
