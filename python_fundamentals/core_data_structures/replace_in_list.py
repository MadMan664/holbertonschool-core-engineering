#!/usr/bin/env python3
"""Module that replaces an element in a list at a given position."""


def replace_in_list(my_list, idx, element):
    """Replace my_list[idx] with element and return my_list.

    If idx is negative or out of range, return my_list unchanged.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
