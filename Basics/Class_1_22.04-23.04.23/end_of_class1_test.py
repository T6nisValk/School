# 1. Area of the triangle
print("Calculate the area of a rectangle.")
length = float(input("Enter the length of a triangle(cm): "))
width = float(input("Enter the width of a triangle(cm): "))
result_1 = length * width
print(f"The area of the rectangle is {round(result_1, 2)} cm.")

# 2. a³ – b³
print("Calculate a³-b³.")
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
result_2 = (a - b)*(a**2 + a*b + b**2)
print(f"{a}³ - {b}³ is equal to {round(result_2, 2)}")

# 3. Area of a circle
print("Calculate the area of a circle.")
pi = 3.14
radius_1 = float(input("Enter the radius of a circle(cm): "))
result_3 = pi * (radius_1**2)
print(f"Area of the circle is {round(result_3, 2)} cm.")

# 4. Volume of a sphere
print("Calculate the volume of a sphere.")
pi = 3.14
radius_2 = float(input("Enter the radius of a sphere(cm): "))
result_4 = (4 * pi * radius_2**3)/3
print(f"Volume of the sphere is {round(result_4, 2)} cm.")

# 5. x² +  y² +  z² – 3xyz
print("Calculate x² +  y² +  z² – 3xyz.")
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))
z = float(input("Enter a value for z: "))
result_5 = (x + y + z)*(x**2 + y**2 + z**2 - x*y - y*z - x*z)
print(f"{x}² + {y}² + {z}² - 3 * {x} * {y} * {z} is equal to {round(result_5, 2)}.")
