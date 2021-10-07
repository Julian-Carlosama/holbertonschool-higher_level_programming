#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Method that inicialized an object """
        width = 0
        height = 0

    @property
    def width(self):
        """ Method that return the width  """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Method that allow create a width """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Method that return the height """
        return(self.__height)

    @width.setter
    def height(self, value):
        """ Method that allow create a height """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value
