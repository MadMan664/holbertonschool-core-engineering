#!/usr/bin/env python3
"""Module for safely printing an integer."""


def safe_print_integer(value):
    """Print value using the {:d} format if it is an integer.

    Returns:
        bool: True if value was printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
