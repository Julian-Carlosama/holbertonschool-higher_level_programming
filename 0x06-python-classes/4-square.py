#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Method that inicialized an object """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ returns the current square area """
        return(self.__size ** 2)

    @property
    def size(self):
        """ Method that set of the object """
        return(self.__size)

    @size.setter
    def size(self, value):
        """ Method """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
