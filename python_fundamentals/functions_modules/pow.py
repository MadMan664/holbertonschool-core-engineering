#!/usr/bin/env python3
"""Compute a to the power of b manually, without ** or imports."""


def pow(a, b):
    """Return a raised to the power of b using a loop."""
    result = 1
    for _ in range(b):
        result *= a
    return result
