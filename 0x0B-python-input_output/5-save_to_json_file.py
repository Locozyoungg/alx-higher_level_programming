#!/usr/bin/python3
"""
Module to write an object to a text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the text file.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    filename_list = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename_list)

    filename_dict = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename_dict)

    try:
        filename_set = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename_set)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

