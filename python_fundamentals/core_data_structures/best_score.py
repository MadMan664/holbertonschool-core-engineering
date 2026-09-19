#!/usr/bin/env python3
"""Module that finds the key with the highest value in a dictionary."""


def best_score(a_dictionary):
    """Return the key with the biggest value, or None if empty/None."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
