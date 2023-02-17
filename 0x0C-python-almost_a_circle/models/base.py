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
            json.dumps(list_dictionaries)
