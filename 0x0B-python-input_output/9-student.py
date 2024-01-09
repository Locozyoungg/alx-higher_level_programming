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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        json_dict = {}
        for key, value in self.__dict__.items():
            if not callable(value) and not key.startswith("__"):
                json_dict[key] = value
        return json_dict

