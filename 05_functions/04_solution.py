#4: Reverse a String.
# Reverse a string using a Loop.

import math

def circle_stats(radius):
    area = math.pi * radius ** 2            # pi*r**2
    circumference = 2 * math.pi * radius    # 2*pi*r
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)