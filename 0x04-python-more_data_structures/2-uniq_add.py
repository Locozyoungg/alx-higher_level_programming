#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    # Create an empty list to store unique integers
    unique_list = []

    # Iterate over the elements in the original list
    for element in my_list:
        # If the element is not already in the unique list, append it
        if element not in unique_list:
            unique_list.append(element)

    # Sum the elements in the unique list to get the result
    result = sum(unique_list)

    return result
