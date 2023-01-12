#!/usr/bin/python3
"""
    Module to create a class Student.
"""


class Student:
    """class creation"""

    def __init__(self, first_name, last_name, age):
        """method creation with 3 attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to retrieve a dictionary representation of Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """method to replace all attributes of Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
