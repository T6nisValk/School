from datetime import datetime


def simple_decorator(function):
    def wrapper():
        print("Before function executes.")
        function()
        print("After function executes.")

    return wrapper


@simple_decorator  # Decorator calls the decorator function.
def example_func():
    print("Doing something ...")


example_func()


# Log the timestamp a function runs.
def log_time(func):
    """
        A Wrapper to log execution time of a function.
    """

    def wrapper():
        # __name__ gives the function name
        print(f"Job {func.__name__} started at: {datetime.today().strftime('%D %H:%M:%S')}")
        func()
        print("Job completed.")

    return wrapper


@log_time
def example():
    print("Working.")


@log_time
def backup():
    print("Backing up.")


example()
backup()


# Decorator for validation.
def validating_non_negative_numbers(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):  # Any() Returns True if any of the numbers in args are
            # negative
            raise ValueError("All parameters must be greater than 0")  # If True raise error
        return func(*args, *kwargs)

    return wrapper


@validating_non_negative_numbers
def sum_2(a, b):
    return a + b


@validating_non_negative_numbers
def sum_all(*args):
    return sum(num for num in args)


print(sum_all(2, 3, 4, 2, 1))
print(sum_2(4, 5))
# print(sum_2(-2, -4))  # Raises a ValueError.
