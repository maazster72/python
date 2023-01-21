"""
This program outputs the surface area of a sphere when given the radius as an input
"""

import math

radius = float(input("Enter the radius of a sphere: "))

surface_area = 4 * math.pi * (radius ** 2)

str_surface_area = "The surface area of the sphere is " + str(surface_area) + " units^2"

print(str_surface_area)