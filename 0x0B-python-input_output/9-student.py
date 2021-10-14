#!/usr/bin/python3
"""
Class that defines a student
"""


class Student:
    """
    Constructor with Public attributes
    that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Public method that retrieves
    a dictionary representation of a Student
    """

    def to_json(self):
        return (self.__dict__)
