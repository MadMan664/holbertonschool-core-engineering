#!/usr/bin/env python3
"""Define the Rectangle class."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle, built on top of BaseGeometry."""

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
