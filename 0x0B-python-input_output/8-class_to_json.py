#!/usr/bin/python3
"""
Module to provide class_to_json function.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary description with simple data structure.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if not callable(value) and not key.startswith("__"):
            json_dict[key] = value
    return json_dict

