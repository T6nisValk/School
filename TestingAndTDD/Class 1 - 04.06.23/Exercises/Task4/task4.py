def _get_data(how_much):
    with open('test_text.txt', 'r') as f:
        return f.read(how_much)


def get_avg(how_much):
    data = _get_data(how_much)
    numbers = [int(x) for x in data]
    return sum(numbers) / len(numbers)


print(get_avg(3))
