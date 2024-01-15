#!/usr/bin/python3
"""Module defining the Base class."""
import json
import csv
import turtle


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
        dummy_instance = cls(1, 1)  # Create a dummy instance with "dummy" mandatory attributes
        dummy_instance.update(**dictionary)  # Update the dummy instance with real values from dictionary
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method to serialize and save instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            csv_writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        row = [obj.id, obj.size, obj.x, obj.y]
                    csv_writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Class method to deserialize and load instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as file:
                csv_reader = csv.reader(file)
                list_objs = []
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dict_values = [int(value) for value in row]
                        list_objs.append(cls.create(**dict(zip(cls.create().__dict__.keys(), dict_values))))
                    elif cls.__name__ == "Square":
                        dict_values = [int(value) for value in row]
                        list_objs.append(cls.create(**dict(zip(cls.create().__dict__.keys(), dict_values))))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method to open a window and draw all the Rectangles and Squares using Turtle graphics."""
        screen = turtle.Screen()
        screen.title("Turtle Drawing")
        screen.setup(width=800, height=600)

        pen = turtle.Turtle()
        pen.speed(1)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
           

