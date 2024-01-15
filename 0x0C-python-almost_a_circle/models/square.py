#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overridden __str__ method to return a formatted string."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

