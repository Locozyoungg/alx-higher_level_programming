#!/usr/bin/python3
"""
Module to create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    filename_list = "my_list.json"
    my_list = load_from_json_file(filename_list)
    print(my_list)
    print(type(my_list))

    filename_dict = "my_dict.json"
    my_dict = load_from_json_file(filename_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        filename_set = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename_set)
        print(my_set)
        print(type(my_set))
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename_fake = "my_fake.json"
        my_fake = load_from_json_file(filename_fake)
        print(my_fake)
        print(type(my_fake))
    except ValueError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

