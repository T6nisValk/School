# Exceptions in Python

## Types of errors

- logical errors
- syntax errors
- runtime errors

## Handling exceptions

- "try" - "except" block

## Error examples

- ZeroDivisionError: divide by zero
- KeyError: When you try to get a value for a key
  that doesn't exist in a dictionary

````python
var = {"1": "Hello", "2": "World"}
print(var["3"])
````

- IndexError: Out of range of available subscripts

````python
var = [1, 2, 3]
print(var[5])
````

- ImportError: Cannot find the method you're trying to import
  from module.
- ModuleNotFoundError: Cannot find the module you're
  trying to import.
- NameError: Trying to access a variable that is not defined.

## Raising exceptions

You want to force a specific exception to occur

````python
raise NameError("Just raising error for the fun")
````

## Finally in try - except block

Finally is executed regardless if an error occurred.
It is run after the try or except block has been executed.

Examples:

- When you open a file for operation, regardless of the outcome
  you want to close the file.
- Open a database connection for operations, you want to close it.

## Guidelines

- Specify the type of Exception to be handled in your
  except block.
- Ensure clear error messages.
- You don't want too many try/except statements. Only use
  when necessary. Ensure you handle outliers appropriately.

## Custom Exception

````python
class ValidationError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


try:
    raise ValidationError("Invalid data passed",
                          {"error1": "integer allowed",
                           "error2": "string allowed"})
except ValidationError as e:
    print(e)
    print(e.error)
````