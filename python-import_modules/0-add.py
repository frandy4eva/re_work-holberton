#!/usr/bin/python3
"""Program that imports the function def add(a, b): from the file add_0.py"""
from test_dir.add_0 import add


def my_add():
    a = 1
    b = 2

    print(f"{a} + {b} = {add(a, b)}")


if __name__ == '__main__':
    my_add()
