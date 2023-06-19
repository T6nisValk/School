# Import as a shorter name
import area as ar
import numpy

# From keyword to import specific function(s)
from perimeter import circle


print("Area of the circle is {}".format(ar.circle(10)))

print(f"Area of the circle is {ar.circle(10)}")

print("Area of the circle is %d" % ar.circle(10))

print(f"Perimeter of the circle is {circle(10)}")
