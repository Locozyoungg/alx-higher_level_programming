#!/usr/bin/python3
"""This module defines a class MagicClass that represents a circle"""

import math


class MagicClass:
    """This class represents a circle with a private attribute radius"""

    def __init__(self, radius=0):
        """This method initializes a circle with a given radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This method returns the current circle area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This method returns the current circle circumference"""
        return 2 * math.pi * self.__radius
