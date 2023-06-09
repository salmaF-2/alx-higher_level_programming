#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    o = argv[2]
    b = int(argv[3])

    if o == '+':
        print("{} {} {} = {}".format(a, o, b, add(a, b)))
    elif o == '-':
        print("{} {} {} = {}".format(a, o, b, sub(a, b)))
    elif o == '*':
        print("{} {} {} = {}".format(a, o, b, mul(a, b)))
    elif o == '/':
        print("{} {} {} = {}".format(a, o, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
