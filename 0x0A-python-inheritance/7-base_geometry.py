#!/usr/bin/python3
"""
class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    Public instance method that raises an Exception.
    """
    pass

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
