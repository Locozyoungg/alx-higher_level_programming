#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element with another in a new list."""
    # Create an empty list to store the new elements
    new_list = []

    # Iterate over each element in the original list
    for element in my_list:
        # Check if the current element is equal to the search element
        if element == search:
            # If yes, append the replace element to the new list
            new_list.append(replace)
        else:
            # If no, append the current element to the new list
            new_list.append(element)

    return new_list
