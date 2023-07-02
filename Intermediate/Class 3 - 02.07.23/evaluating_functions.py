import functools
import tracemalloc
from time import perf_counter


# Performance measure - Computes the memory consumed by a function and the speed of the function

# Balance tradeoff between speed and memory.

def performance_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, *kwargs)
        current, peak = tracemalloc.get_traced_memory()
        end_time = perf_counter() - start_time
        print(f"Function: {func.__name__} ")
        print(f"Function: {func.__doc__} ")
        print(f"Peak memory usage: \t\t{peak / 10 ** 6:.7f} MB")  # \t - Tab
        print(f"Current memory usage: \t\t{current / 10 ** 6:.7f} MB")  # :.f decimal points.
        print(f"Time it took: \t\t{end_time:.7f}")

    return wrapper


# Returns list of numbers numbers from 0 to 1000
@performance_measure
def using_range():
    """
    Using range
    """
    list_var = list(range(1000000))
    return list_var


@performance_measure
def using_comprehension():
    """
    Using comprehension
    """
    list_var = [num for num in range(1000000)]
    return list_var


@performance_measure
def using_list_append():
    """
    Using list append
    """
    list_var = []
    for num in range(1000000):
        list_var.append(num)
    return list_var


print("---\n")
using_range()
print("---\n")
using_comprehension()
print("---\n")
using_list_append()
