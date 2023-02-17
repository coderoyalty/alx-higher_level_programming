#!/usr/bin/python3
'''
    Define square class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Module for a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
            size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            size setter
            Arguments:
                @value new size
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
            overloading the str method.
        '''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y,
            self.width
        )
