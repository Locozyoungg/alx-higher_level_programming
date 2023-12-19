#!/usr/bin/python3
"""This module defines a class Square that defines a square"""


class Square:
    """This class represents a square with a private attribute size"""

    def __init__(self, size=0):
        """This method initializes a square with a given size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
