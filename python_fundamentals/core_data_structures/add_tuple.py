#!/usr/bin/env python3
"""Module that adds two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a new 2-element tuple summing tuple_a and tuple_b.

    Missing values are treated as 0; extra values beyond the
    first two are ignored.
    """
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return (a[0] + b[0], a[1] + b[1])
