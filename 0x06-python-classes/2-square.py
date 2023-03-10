#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """Class that defines a Square"""
    def __init__(self, size=0):
        """
            Initializing this square class.
        """

        if type(size) is not int:
            raise TypeError ("size must be an integer")

        if size < 0:
            raise ValueError ("size must be >= 0")

        self.__size = size
