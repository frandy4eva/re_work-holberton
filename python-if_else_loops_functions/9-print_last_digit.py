#!/usr/bin/python3
def print_last_digit(number):
    """Function that prints the last digit of a number"""
    number = abs(number)
    print(number % 10, end='')
    return number % 10
