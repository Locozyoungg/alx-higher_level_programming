#!/usr/bin/python3
"""Module defining the Base class."""
import json

class Base:
    """Base class for managing id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is not None:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
            else:
                list_dicts = []
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Static method to return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Class method to return an instance with all attributes already set."""
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance
  
    @classmethod
    def load_from_file(cls):
        """Class method to return a list of instances from a file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                list_objs = [cls.create(**obj) for obj in list_dicts]
                return list_objs
        except FileNotFoundError:
            return []

