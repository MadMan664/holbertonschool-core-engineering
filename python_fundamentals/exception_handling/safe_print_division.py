#!/usr/bin/env python3
"""Module for safely dividing two integers."""


def safe_print_division(a, b):
    """Divide a by b, always reporting the result via finally.

    Returns:
        The division result, or None if the division failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
