#!/usr/bin/env python3
"""Define the Square class."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a specialized rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the length of the square's side. Must be a
                positive integer.
        """
        super().__init__(size, size)
