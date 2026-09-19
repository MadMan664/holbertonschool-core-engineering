#!/usr/bin/env python3
"""Compute a to the power of b manually, without ** or imports."""


def pow(a, b):
    """Return a raised to the power of b using a loop."""
    exponent = -b if b < 0 else b
    result = 1
    for _ in range(exponent):
        result *= a
    if b < 0:
        result = 1 / result
    return result
