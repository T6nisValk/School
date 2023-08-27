def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero. You should know that.."


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(division(a, b))
