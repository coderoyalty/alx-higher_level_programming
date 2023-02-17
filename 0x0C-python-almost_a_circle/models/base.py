#!/usr/bin/python3
"""
    Creating the base class of all other classes for this project.
"""
import json


class Base:
    '''
        This class will manage the id attribute of all the classes.
        Arguments:
            @id: The id for a specific instance.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def validator(attribute, value):
        '''
            static method to validates an attribute of rectangle
            Arguments:
                @attribute: the attribute to check for.
                @value: the value passed
        '''

        if type(value) != int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute in ["x", "y"]:
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            static method to convert a dictionary to
            json string.
            Arguments:
                @list_dictionaries: list of dictionaries
        '''

        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            static method to save a dictionary to file
        '''

        buffer = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_obj = json.loads(cls.to_json_string(item))
                buffer.append(json_obj)
        with open(filename, mode="w") as file:
            json.dumps(buffer, file)
