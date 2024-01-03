#!/usr/bin/python3
"""
This module contains a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds 2 integers and returns the result
    Args:
        a (int or float): the first operand
        b (int or float): the second operand (default: 98)
    Returns:
        int: the sum of a and b as an integer
    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
