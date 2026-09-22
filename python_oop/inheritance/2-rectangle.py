#!/usr/bin/env python3
"""Define a full Rectangle class with an area and a string form."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with an area and a readable form."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the rectangle's width. Must be a positive
                integer.
            height (int): the rectangle's height. Must be a positive
                integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle as [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
