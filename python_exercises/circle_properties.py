"""
This program takes a radius as an input and outputs the circumference and area of a circle
"""

import math

radius = float(input("Enter the radius of a cirlce: "))

circum = 2 * math.pi * radius
area = math.pi * (radius ** 2)

str_circum = "The circumference of the cirlce is " + str(circum) + " units"
str_area = "The area of the circle is " + str(area) + " units^2"

print(str_circum)
print(str_area)
