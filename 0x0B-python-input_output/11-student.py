#!/usr/bin/python3
"""
Module to provide Student class.
"""

class Student:
    """
    Student class definition.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings specifying the attributes to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        json_dict = {}
        if attrs is None:
            attrs = self.__dict__.keys()
        for key, value in self.__dict__.items():
            if key in attrs:
                json_dict[key] = value
        return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a provided dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs to reload.
        """
        for key, value in json.items():
            setattr(self, key, value)

