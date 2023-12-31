# Decorators (`decorators.py`)

Decorators allow programmers to modify the behaviour of a function or a class without
modifying the code itself.

Allows us to wrap a function with another function in order to extend the behaviour of
the wrapped function.

Examples where decorators are used:

- Logging
- To test performance
- Cache
- Verify premissions
- Decimal places of floating numbers

### Building blocks for decorators

- A function is an instance of the object type. A function is an object, because we
  can store a function in a variable.
- A function can be passed as an argument to another function.
- A function can be nested within another function.
- A nested function can be returned.

### Syntax for a decorator (`decors.py`)

````
def decorator_function_name(func):
    def wrapper_function():
        return func + 5  # Do something

    return wrapper_function


# To use a decorator syntax:
@decorator_function_name
def my_function():
    pass

````

# Decorators with arguments (`decorator_args.py`)

To create a decorator that gets an argument, you need to create a function that returns a
decorator rather than writing the decorator directly.

````
def function_that_returns_decorator(*arguments):
    def decorator_function_name(func):
        def wrapper_function():
            print({arguments})
            func()  # Do something

        return wrapper_function

    return decorator_function_name


@function_that_returns_decorator(2, 3)
def my_func():
    pass

````

# Chaining decorators (`decorator_chain.py`)

Can apply more than 1 decorator to a function. Apply it from bottom to top.

````
@decorator1
@decorator2
def function():
    pass
````