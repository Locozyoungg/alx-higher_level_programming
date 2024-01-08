#!/usr/bin/python3
"""Module containing Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize the square with the given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

if __name__ == "__main__":
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())

