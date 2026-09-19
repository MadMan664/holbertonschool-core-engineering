#!/usr/bin/env python3
"""Import arithmetic functions and print the results of each operation."""
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    result = div(a, b)
    if result == int(result):
        result = int(result)
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, result))
