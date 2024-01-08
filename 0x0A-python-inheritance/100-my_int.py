#!/usr/bin/python3
"""Module containing MyInt class"""


class MyInt(int):
    """A class representing a rebellious integer."""

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)

if __name__ == "__main__":
    MyInt = __import__('100-my_int').MyInt

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

