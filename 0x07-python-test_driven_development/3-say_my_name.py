#!/usr/bin/python3
"""
This module contains a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Args:
        first_name (str): the first name
        last_name (str): the last name (default: "")
    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
