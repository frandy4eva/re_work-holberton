#!/usr/bin/python3
"""Print specific output based on random number"""
from random import randint
number = randint(-10000, 10000)
number = abs(number)
last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
elif last_digit < 6:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not zero")
