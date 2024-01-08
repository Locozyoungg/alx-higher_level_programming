#!/usr/bin/python3
"""Module containing is_same_class function"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

if __name__ == "__main__":
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

