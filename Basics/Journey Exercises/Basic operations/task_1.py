import math


def circle_area_to_price(radius, price):
    area = math.pi * radius ** 2
    return area / price


print(f"Pizza one with the price of 20 and radius of 5: {circle_area_to_price(5, 20)}")
print(f"Pizza two with the price of 13 and radius of 9: {circle_area_to_price(9, 13)}")
