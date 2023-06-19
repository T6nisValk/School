def hello(value="World!"):  # Default value given if function call has no value.
    print(f"Hello {value}")


hello()


def sum_of_numbers(should_do, message, *args):
    result = 0
    for arg in args:
        result += arg

    if should_do:
        print(message, result)


sum_of_numbers(True, "A sum is: ", 2, 3)


# x = lambda a, b, c : a + b + c
# print(x(3, 4, 5))

def multiple_arguments_named_values_assignment(num1, num2, num3, num4):
    print(f"{num1 + num2 + num3 + num4}")


multiple_arguments_named_values_assignment(1, 2, 3, 4)
multiple_arguments_named_values_assignment(num1=1, num3=3, num4=4, num2=2)
multiple_arguments_named_values_assignment(1, 2, num4=4, num3=3)


def total_args(*args):
    print(args)
    for text in args:
        print(text.upper())


total_args("Text1", "Text2", "Text3", "Text4")


def total_args_with_optional_arg(*args, end):
    for text in args:
        print(text, end=end)


total_args_with_optional_arg("Text1", "Text2", "Text3", "Text4", end=" ")

print("\n")


def total_args_with_required_and_optional_arg(start, *args, end=" "):
    for text in args:
        print(f"{start} - {text}", end=end)


total_args_with_required_and_optional_arg("Some text", "Text1", "Text2", "Text3", "Text4")
print("\n")


def total_kwargs(**kwargs):  # key word arguments
    result = 0
    for key in kwargs:
        print(f"{key} - {kwargs[key]}", end=" ")
        result += kwargs[key]
    print("\n", result)


total_kwargs(eggs=5, potatoes=3, bacon_strips=2, bread=2, cheese=2)


def total_kwargs_with_optional_arg(milk=1, **kwargs):  # Optional only works before **kwargs
    result = 0
    for key, value in kwargs.items():
        print(f"{key} - {value}", end=" ")
        result += value
    print("\n", result, end=f" {milk}")


total_kwargs_with_optional_arg(eggs=5, potatoes=3, bacon_strips=2, bread=2, cheese=2)

print("\n")


def total_kwargs_with_required_and_optional_arg(arg1, potato=5, **kwargs):
    result = 0
    for key, value in kwargs.items():
        result += value
    print(f"{arg1}: {result}", end=f" {potato} \n")


total_kwargs_with_required_and_optional_arg("Required argument", 9, eggs=5, potatoes=3, bacon_strips=2)
total_kwargs_with_required_and_optional_arg(arg1="Required argument", potato=9, eggs=5, potatoes=3, bacon_strips=2)
total_kwargs_with_required_and_optional_arg(potato=9, potatoes=3, eggs=5, arg1="Required argument", bacon_strips=2)


def total_args_and_kwargs(*args, **kwargs):
    result = 0
    for number in args:
        result += number
    for key, value in kwargs.items():
        result += value
    print(result)


total_args_and_kwargs(1, 1, 1, eggs=2, bacon=2)


def total_args_and_kwargs_with_optional_arg(potato, *args, **kwargs):
    result = 0
    for number in args:
        result += number
    for key, value in kwargs.items():
        result += value
    print(result + potato)


total_args_and_kwargs_with_optional_arg(4, 1, 1, 1, eggs=2, bacon=2)
print("\n")
print("-------------------------Return functions-------------------------")


def add(a, b):
    return a + b


print(add(1, 2))




def sum1(items):
    print("-------------------------SUM functions----------------------------")
    result = 0
    for item in items:
        result += item
    return result


print(sum1([1, 1, 1, 1, 1]))
