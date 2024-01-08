#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """An empty class."""
    pass

if __name__ == "__main__":
    BaseGeometry = __import__('5-base_geometry').BaseGeometry

    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))

