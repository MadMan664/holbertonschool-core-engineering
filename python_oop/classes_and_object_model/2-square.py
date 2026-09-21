#!/usr/bin/env python3
"""Define a Square class with a validated private size attribute."""


class Square:
    """Represent a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the length of the square's side. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
