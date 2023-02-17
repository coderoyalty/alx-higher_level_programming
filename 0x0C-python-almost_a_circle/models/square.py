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

    def update(self, *args, **kwargs):
        '''
            update module
        '''
        args_len = len(args)
        if args_len == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return
        else:
            for npos, arg in enumerate(args):
                if npos == 0:
                    self.id = arg
                elif npos == 1:
                    self.size = arg
                elif npos == 2:
                    self.x = arg
                elif npos == 3:
                    self.y = arg
