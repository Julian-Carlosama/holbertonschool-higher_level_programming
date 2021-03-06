#!/usr/bin/python3
"""
Rectangle class that inherits from Base
Private instance attributes, each with its
own public getter and setter
"""


from models.base import Base
"""
Import the base class
"""


class Rectangle(Base):
    """Rectangle method"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inicialized constructor
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return self"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """to retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return a string"""
        return(f"[Rectangle] \
({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        method that assigns an
        argument to each attribute:
        """
        if args is not None and len(args) != 0:
            my_list = ["id", "width", "height", "x", "y"]
            for j in range(len(args)):
                setattr(self, my_list[j], args[j])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
