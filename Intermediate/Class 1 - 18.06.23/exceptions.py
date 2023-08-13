# Try - Except block
# while True:
#     try:  # Try to run, if no error, continue
#         print("Divide 10")
#         # num = int(input("Enter a number you want to divide 10 with: "))
#         print(10 / 0)
#         break
#     except ZeroDivisionError:  # Specific error handling
#         print("Cant dicide by zero.")
#         break
#     except Exception as err:  # Catches any error to a variable.
#         print(f"Error {type(err)} occured.")  # Without type() it shows just the error message.
#         break
#     finally:
#         print("Hello")


class ValidationError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


try:
    raise ValidationError(
        "Invalid data passed", {"error1": "integer allowed", "error2": "string allowed"}
    )
except ValidationError as e:
    print(e)
    print(e.error)
