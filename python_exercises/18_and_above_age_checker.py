"""
This program takes an age as an input and returns a boolean true if age is greater than 17 or false if less than 18
"""

age = int(input("Please enter an age: "))
over18 = False
if (age > 17):
    over18 = True

print(over18)
