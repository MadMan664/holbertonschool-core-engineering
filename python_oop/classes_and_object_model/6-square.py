#!/usr/bin/env python3
"""Define a Square class with a position and a string representation."""


class Square:
    """Represent a square with a size, a position, and a string form."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): the length of the square's side. Defaults to 0.
            position (tuple): the (x, y) offset used when printing.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, validating it.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(v) is int for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#', offset according to position.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the same rendering my_print() prints, as a string."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        lines += [(" " * self.__position[0]) +
                  ("#" * self.__size)] * self.__size
        return "\n".join(lines)
