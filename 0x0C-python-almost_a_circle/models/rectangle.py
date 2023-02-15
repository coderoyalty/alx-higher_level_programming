#!/usr/bin/python3
"""
    Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            __width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            __height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            __x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            set private attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

	@property
    def y(self):
        '''
            __y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            set private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value
