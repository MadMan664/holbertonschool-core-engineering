#!/usr/bin/env python3
"""Define a Square class with its own string representation."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a readable [Square] form."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the length of the square's side. Must be a
                positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square as [Square] <width>/<height>."""
        return super().__str__().replace("Rectangle", "Square", 1)
