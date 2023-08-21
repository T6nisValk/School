def calculator_2_0():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    op = input("Enter the operator: ")
    return f"{x} {op} {y} = {eval(f'{x}{op}{y}')}"


print(calculator_2_0())
