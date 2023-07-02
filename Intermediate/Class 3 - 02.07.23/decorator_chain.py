def decorator1(func):
    def wrapper():
        print("Decorator 1 before function.")
        func()
        print("Decorator 1 after function.")

    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2 before function.")
        func()
        print("Decorator 2 after function.")

    return wrapper


@decorator1
@decorator2
def hello():
    print("Hello")


# Both act the same way.
decorator1(decorator2(hello()))
print("-" * 100)
hello()

print("-" * 100)


# Another example
def print_star(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)

    return wrapper


def print_hash(func):
    def wrapper(*args, **kwargs):
        print("#" * 10)
        func(*args, **kwargs)
        print("#" * 10)

    return wrapper


# print_star(print_hash(print_something("Hello")))
@print_star
@print_hash
def print_something(message):
    print(message)


print_something("Hello")

print("-" * 100)


# print_hash(print_star(print_something("Hello")))
@print_hash
@print_star
def print_something(message, name):  # *args, **kwargs in decorator function.
    print(f"{message}, {name}")


print_something("Hello", "Me")
