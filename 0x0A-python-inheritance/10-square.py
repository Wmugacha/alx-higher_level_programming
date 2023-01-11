#!/usr/bin/python3
"""
    Inherits from class Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size):
        """Method to instantiate size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
