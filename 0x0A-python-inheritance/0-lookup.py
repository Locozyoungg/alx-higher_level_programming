#!/usr/bin/python3
"""Module with function to get attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list object with the available attributes and methods of an object.

    Args:
        obj (object): The object to lookup.

    Returns:
        list: List containing the attributes and methods of the object.
    """
    return dir(obj)

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))

