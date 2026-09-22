#!/usr/bin/env python3
"""Define an abstract Shape class, concrete shapes, and shape_info."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Represent a generic shape with an area and a perimeter."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""


class Circle(Shape):
    """Represent a circle defined by its radius."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (float): the circle's radius.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (float): the rectangle's width.
            height (float): the rectangle's height.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of shape, via duck typing.

    Args:
        shape: any object providing area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
