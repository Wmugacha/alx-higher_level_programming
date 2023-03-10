#!/usr/bin/python3
"""Module that defines a Square"""


class Square:
    """Class that defines a Square"""

    def __init__(self, size=0):
        """Initializing this square class.

        Args:
            size: represents the size of the square deined.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
