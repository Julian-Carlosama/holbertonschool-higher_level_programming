#!/usr/bin/python3
"""  class that defines a rectangle """


class Rectangle:
    """ Class rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Method that inicialized an object """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return(salto)

        for i in range(self.height):
            salto += ((self.width) * str(self.print_symbol)) + "\n"
            rectangle = salto[:-1]

        return(rectangle)

    def __repr__(self):
        """ Method that return a string """
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return(rep)

    def __del__(self):
        """ Method that Print the message Bye rectangle. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
