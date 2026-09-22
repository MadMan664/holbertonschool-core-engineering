#!/usr/bin/env python3
"""Define the BaseGeometry class."""


class BaseGeometry:
    """Represent shared behavior for geometric shapes."""

    def area(self):
        """Raise an exception; subclasses must implement this."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name used in the error messages.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
