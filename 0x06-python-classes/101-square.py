#!/usr/bin/python3
"""This module defines a class Square that defines a square"""


class Square:
    """This class represents a square with a private attribute size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes a square with a given size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This property returns the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This property setter sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This property returns the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This property setter sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """This method returns the printable representation of the square"""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for i in range(self.__position[1]):
                result += "\n"
            for i in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result[:-1]
