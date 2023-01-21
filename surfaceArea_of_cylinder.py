"""
This program outputs the surface area of a cylinder when given the radius and height as an input
"""

import math

radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = 2 * math.pi * radius * (radius + height)

str_surface_area = "The surface area of the cylinder is " + str(surface_area) + " units^2"

print(str_surface_area)