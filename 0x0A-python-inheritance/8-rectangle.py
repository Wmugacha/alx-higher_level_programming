#!/usr/bin/python3

"""
    Module that creates a class BaseGeometry.
"""


class BaseGeometry:
    """Class that represents BaseGeometry"""

    def area(self):
        """Method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Method to instantiate width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
