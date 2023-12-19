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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
