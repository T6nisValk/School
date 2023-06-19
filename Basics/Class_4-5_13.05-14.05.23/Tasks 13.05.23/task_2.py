# Task 2: Create a function in such a way that we can pass any number of arguments to this function,
# and the function should process them and display each argument’s value.

def argument_test(*args):
    for arg in args:
        print(f"{arg}", end="\n")


argument_test("Hello", "World", 312, "!")
