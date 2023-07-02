from datetime import datetime


# Decorator for functions that runs between specific hours of the day
def run_between_hours(from_time=8, to_time=17):  # Function that returns decorator
    def between_hours(func):  # Decorator
        def wrapper():  # Wrapper
            if from_time <= datetime.now().hour <= to_time:
                func()

        return wrapper

    return between_hours


@run_between_hours(12, 13)
def print_something():
    print("I am here")


print_something()

something = 0


# Repetition example
def repeat(num_of_repeats):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            global something
            if num_of_repeats == 0:
                raise NameError("Can't have zero")
            for i in range(num_of_repeats):
                something = func(*args, **kwargs)
            return something

        return wrapper

    return decorator_repeat


@repeat(0)
def my_func():
    print("On repeat.")


my_func()
