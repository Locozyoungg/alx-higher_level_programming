#!/usr/bin/python3
"""This module defines a class Square that defines a square"""


class Square:
    """This class represents a square with a private attribute size"""

    def __init__(self, size=0):
        """This method initializes a square with a given size"""
        self.size = size

    @property
    def size(self):
        """This property returns the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This property setter sets the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """This method compares two squares for equality based on their area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """This method compares two squares for inequality based on their area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """This method compares two squares for less than relation based on their area"""
        return self.area() < other.area()

    def __le__(self, other):
        """This method compares two squares for less than or equal relation based on their area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """This method compares two squares for greater than relation based on their area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """This method compares two squares for greater than or equal relation based on their area"""
        return self.area() >= other.area()
