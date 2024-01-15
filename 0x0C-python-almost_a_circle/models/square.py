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

    def update(self, *args, **kwargs):
        """Public method to update attributes."""
        attr_list = ['id', 'size', 'x', 'y']

        if args:
            for idx, arg in enumerate(args):
                setattr(self, attr_list[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Overridden __str__ method to return a formatted string."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

