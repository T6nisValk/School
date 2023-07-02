# Functools - functional tools.
import functools

# Class-based decorator
"""
We are using a function called wrap, update_wrapper in functools, because it ensures that the 
decorator mimics the calling functions. Has the same name(__name__), docs(__doc__) as the wrapper.
"""


# Count how many times an action is called.
class CountNumOfCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    # Magic method, that allows the class instances to be called as a function
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Called function {self.func.__name__} {self.calls} times")
        return self.func(*args, *kwargs)


@CountNumOfCalls
def say_something(name):
    print(f"Hello {name}")


say_something("Someone")
say_something("Someone Else")


def limit_calls(max_calls):
    num_calls = {"count": 0}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if num_calls["count"] >= max_calls:
                raise Exception("Max amount reached")
            num_calls["count"] += 1
            return func(*args, *kwargs)

        return wrapper

    return decorator


@limit_calls(2)
def my_func(name):
    print(f"{name}")


my_func("Hello")
my_func("My")
my_func("friend")
