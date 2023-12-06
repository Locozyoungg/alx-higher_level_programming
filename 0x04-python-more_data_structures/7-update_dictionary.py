#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary."""
    # Update the value if the key exists, otherwise, create a new key-value pair
    a_dictionary[key] = value
    return a_dictionary
