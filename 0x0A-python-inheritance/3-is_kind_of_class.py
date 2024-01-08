#!/usr/bin/python3
"""Module containing is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)

if __name__ == "__main__":
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

