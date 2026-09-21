#!/usr/bin/env python3
"""Define a Square class that can print itself."""


class Square:
    """Represent a square that can render itself with '#'."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the length of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
