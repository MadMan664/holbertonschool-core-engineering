#!/usr/bin/env python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each row of matrix on its own line, values space-separated."""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
