#!/usr/bin/python3
"""  class that defines a rectangle """


class Rectangle:
    """ Class rectangle """
    def __init__(self, width=0, height=0):
        """ Method that inicialized an object """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that return the width  """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Method that allow create a width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Method that return the height """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ Method that allow create a height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return(self.width * self.height)

    def perimeter(self):
        """  Public instance method that returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return(0)
        return((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ Method that allow """
        salto = ""
        if self.width and self.height == 0:
            return(salto)

        for i in range(self.height):
            salto += ("#" * self.width) + "\n"
            rectangle = salto[:-1]

        return(rectangle)
