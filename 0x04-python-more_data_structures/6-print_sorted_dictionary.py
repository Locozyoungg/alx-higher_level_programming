#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
