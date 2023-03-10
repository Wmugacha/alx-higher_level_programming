#!/usr/bin/python3
"""Module that defines a Square"""


class Square:
    """Class that defines a Square"""

    def __init__(self, size=0):
        """Initializing this square class.

        Args:
            size: represents the size of the square defined.
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

    def area(self):
        """method that returns area of the square.

        Returns: Area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """To retrieve size attribute"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """setter property to set the value of square size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """Method to print the square to stdout with #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                print()
