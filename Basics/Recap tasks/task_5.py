"""
This equation x2 + y2 + z2 - 3xyz formula: (x + y + z)(x2 + y2 + z2 - xy - yz -xz)
"""


def math_formula(x, y, z):
    return (x + y + z) * ((x**2) + (y**2) + (z**2) - (z * y) - (y * z) - (x * z))
