#!/usr/bin/python3
"""
Class principal called base
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ inicialized a constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
