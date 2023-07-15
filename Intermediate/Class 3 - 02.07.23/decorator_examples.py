# Example 1 - Logging and timing
import datetime
import logging
import time

print("-" * 120)


def logging_and_timing(func):
    def wrapper(*args):
        print(f"{func.__name__} started.")
        print(f"sum {args} = {func(*args)}")
        print(f"{func.__name__} completed.")

    return wrapper


@logging_and_timing
def add(a, b):
    return a + b


add(5, 4)
print("-" * 120)


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"{datetime.date.today()}: {func.__name__} ran for {end - start} secs")
        return output

    return wrapper


@timing_decorator
def increment_2():
    for i in range(0, 100000, 2):
        pass


increment_2()
print("-" * 120)


# Example 2: Decorators with arguments - delay

def delay_for_seconds_decorator(delay_time):
    def wrapper(func):
        def inner_function(*args, **kwargs):
            print(f"Waiting for {delay_time} seconds before running {func.__name__}")
            time.sleep(delay_time)
            output = func(*args, **kwargs)
            return output

        return inner_function

    return wrapper


@delay_for_seconds_decorator(0)
def print_my_name(name):
    print(f"My name is {name.upper()}")


print_my_name("tõnis")
print("-" * 120)


# Example 3: Exception handler

def exception_handler(exception_type, message="An error."):
    def wrapper(func):
        def inner_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type:
                logging.error(datetime.date.today())
                return message

        return inner_function

    return wrapper


@exception_handler(ZeroDivisionError, "Can't divide by zero..")
def division(a, b):
    return a / b


print(division(5, 0))
