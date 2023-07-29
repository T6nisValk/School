def create_phone_number(numbers):
    if len(numbers) == 11:
        phone = f"+{numbers[0]}{numbers[1]} " \
                f"{numbers[2]}{numbers[3]}{numbers[4]}-" \
                f"{numbers[5]}{numbers[6]}{numbers[7]}-" \
                f"{numbers[8]}{numbers[9]}{numbers[10]}"
        return phone
    else:
        return "Wrong amount of numbers."


def create_phone(numbers):
    if len(numbers) == 11:
        numbers = [str(num) for num in numbers]
        numbers.insert(0, "+")
        numbers.insert(3, " ")
        numbers.insert(7, "-")
        numbers.insert(11, "-")
    else:
        return "Wrong amount of numbers."
    return "".join(numbers)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 9]))
print(create_phone([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 9]))
