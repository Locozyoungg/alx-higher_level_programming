#!/usr/bin/python3
"""Module containing inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

if __name__ == "__main__":
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

