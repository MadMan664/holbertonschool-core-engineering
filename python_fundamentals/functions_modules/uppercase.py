#!/usr/bin/env python3
"""Print a string converted to uppercase using ASCII logic."""


def uppercase(str):
    """Print str converted to uppercase, without using .upper()."""
    result = ""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print("{}".format(result))
