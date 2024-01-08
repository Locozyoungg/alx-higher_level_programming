#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """A class with an area method."""
    
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

if __name__ == "__main__":
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

