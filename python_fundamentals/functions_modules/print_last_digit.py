#!/usr/bin/env python3
"""Print and return the last digit of a number, always positive."""


def print_last_digit(number):
    """Print the (always positive) last digit of number and return it."""
    last_digit = number % 10
    if number < 0 and last_digit != 0:
        last_digit -= 10
    positive_digit = abs(last_digit)
    print(positive_digit)
    return positive_digit
