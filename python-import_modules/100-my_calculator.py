from calculator_1 import add, sub, mul, div
import sys


def my_calculator():
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))


if __name__ == '__main__':
    my_calculator()
