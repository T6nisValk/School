# Passing a function to a variable.
def shout(text):
    return text.upper()


yell = shout
print(yell("Using shout function to capitalize all the characters"))


# Passing a function to another functions argument.
def add_5(a_var):
    return a_var + 5


def a():
    return 8


print(add_5(a()))


# Nesting example
def outer_func():  # Main function.
    def inner_func():  # Inner function within the outer function.
        print("This is the inner function calling.")

    print("This is the outer function calling")
    inner_func()  # Calling the inner function.


outer_func()


# Returning the inner function example.
def outer_function():
    book = "Angels and demons"

    def inner_function():
        print(f"From inner: {book}")

    return inner_function()  # Returning the inner function.


outer_function()  # Call the function


def double_it(b):
    double = b * 2

    def add_d(d):
        print(double + d)

    return add_d  # Need to return without parenthesis, if function expects a value


for_20 = double_it(20)
for_20(4)
