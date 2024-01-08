#!/usr/bin/python3
"""Module containing MyList class"""


class MyList(list):
    """Inherits from list with additional methods"""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))

if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)

