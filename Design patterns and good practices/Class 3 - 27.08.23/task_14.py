import time
from functools import reduce


def timing_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Time it took to run the function: {str(end_time-start_time)}")

    return wrapper


@timing_function
def factorial(n):
    values = list(range(1, n + 1))
    result = reduce(lambda x, y: x * y, values)
    return result


factorial(500)
