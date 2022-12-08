#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    """program that imports all functions from the
        file calculator_1.py and handles basic operations"""

if len(sys.argv) - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = {"+": add, "-": sub, "*": mul, "/": div}
if sys.argv[2] not in list(operator.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

print("{} {} {} = {}".format(a, sys.argv[2], b, operator[sys.argv[2]](a, b)))
