#!/usr/bin/python3
"""Module that defines a Square"""


class Square:
    """Class that defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class.

        Args:
            size: represents the size of the square defined.
            position: represents x and y position of a square.
        Raises:
            TypeError: if size is not an integer or if position is not a
                        tuple of two integers.
            ValueError: if size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2\
            or not isinstance(position[0], int) or not\
                isinstance(position[1], int) or position[0] < 0\
                or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """method that returns area of the square.

        Returns: Area of the square
        """

        return (self.__size ** 2)

    @property
    def position(self):
        """To retrieve position attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        """setter property to set the value of position attribute"""

        if not isinstance(value, tuple) or len(value) != 2\
            or not isinstance(value[0], int) or not isinstance(value[1], int)\
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    @property
    def size(self):
        """To retrieve size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter property to set the value of square size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def __str__(self):
        """return the square in string format"""

        if self.__size == 0:
            return ""
        else:
            result = ""
            result += "\n" * self.position[1]
            for i in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size
                if i != self.__size - 1:
                    result += "\n"
            return result

        return f"Square({self.__size}, {self.__position})"

    def my_print(self):
        """Method to print the square to stdout with #"""

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
