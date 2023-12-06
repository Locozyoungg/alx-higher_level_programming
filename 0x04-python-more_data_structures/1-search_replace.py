#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element with another in a new list."""
    # Create a new list using list comprehension with replacement
    new_list = [replace if element == search else element for element in my_list]
    return new_list
