#!/usr/bin/env python3
"""Module for printing only the integers found in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list, skipping non-integers.

    All printed integers appear on the same line. x is not
    guarded against exceeding the length of my_list; indexing
    past the end of my_list is allowed to raise IndexError.

    Returns:
        int: the number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
