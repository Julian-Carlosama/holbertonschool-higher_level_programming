#!/usr/bin/python3
'''
Module 10-student
Has a class Student
istantiation with self, first_name, last_name, age
the class contains Public method def to_json(self)
'''


class Student():
    '''
    class Student that defines a student by
    '''

    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        new_dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str and hasattr(self, i):
                    new_dic[i] = getattr(self, i)
                else:
                    pass
        else:
            new_dic = self.__dict__
        return (new_dic)

    def reload_from_json(self, json):
        for i in json:
            for j in self.__dict__:
                if i is j:
                    setattr(self, i, json[i])
