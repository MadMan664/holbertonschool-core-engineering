#!/usr/bin/env python3
"""Module for safely printing a limited number of list elements."""


def safe_print_list(my_list=[], x=0):
    """Print the first x elements of my_list on one line.

    x may exceed the length of my_list; printing stops gracefully
    once the list is exhausted.

    Returns:
        int: the real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
