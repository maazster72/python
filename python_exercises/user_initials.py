"""
This program takes a user's first name and last names as inputs and returns their intials
"""

fname = str(input("Please enter your firstname: "))
lname = str(input("Please enter your surname: "))

initials = fname[0].upper()+lname[0].upper()
print(initials)