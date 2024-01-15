#!/usr/bin/python3
"""Module defining the Rectangle class."""

class Rectangle:
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id if id is not None else 0

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters to stdout."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Overridden __str__ method to return a formatted string."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes based on arguments."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

