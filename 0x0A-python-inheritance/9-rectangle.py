#!/usr/bin/python3
"""
    Inherits from class BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Method to instantiate width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
