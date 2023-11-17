
"""Program that imports functions from the file calculator_1.py, does some Maths, and prints the result."""

from test_dir.calculator_1 import add, sub, mul, div, mod

if __name__ == '__main__':
    a = 15
    b = 2

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b):.2f}")
    print(f"{a} % {b} = {div(a, b):.2f}")
