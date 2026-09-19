#!/usr/bin/env python3
"""Print whether a random number is positive, zero, or negative."""
number = __import__('random').randint(-10, 10)

if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
