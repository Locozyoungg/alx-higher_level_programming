#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Overridden __str__ method to return a formatted string."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

