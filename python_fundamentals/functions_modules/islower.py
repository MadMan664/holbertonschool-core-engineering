#!/usr/bin/env python3
"""Check whether a character is a lowercase ASCII letter."""


def islower(c):
    """Return True if c is a lowercase letter, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')
