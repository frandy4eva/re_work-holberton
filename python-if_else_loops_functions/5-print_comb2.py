#!/usr/bin/python3
"""Prints numbers from 0 to 99 with two digits separated by comma except 99"""
for number in range(100):
    if number == 99:
        print(f"{number}\n", end='')
    else:
        print(f"{number:02d}", end=", ")
