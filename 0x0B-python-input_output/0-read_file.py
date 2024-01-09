#!/usr/bin/python3
"""
Module to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    Args:
        filename (str): The name of the text file.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")

