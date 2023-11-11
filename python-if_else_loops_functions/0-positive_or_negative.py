#!/usr/bin/python3
"""Assign random number to variable number"""
from random import randint
number = randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
