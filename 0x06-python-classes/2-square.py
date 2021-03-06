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
