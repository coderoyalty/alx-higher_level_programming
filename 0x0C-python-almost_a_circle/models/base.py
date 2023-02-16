#!/usr/bin/python3
"""
    Creating the base class of all other classes for this project.
"""


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
        if type(value) != int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute is in ["x", "y"] and value < 0:
            raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")
