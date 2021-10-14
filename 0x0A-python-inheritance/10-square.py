#!/usr/bin/python3
"""
class Rectangle that inherits from Rectangle (9-rectangle).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Method that inicialized a square

    super():
    Call atributes of rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
