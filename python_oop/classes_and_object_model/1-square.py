#!/usr/bin/env python3
"""Define a Square class with a private size attribute."""


class Square:
    """Represent a square with a private instance attribute size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of the square's side.
        """
        self.__size = size
