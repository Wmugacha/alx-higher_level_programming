#!/usr/bin/python3
"""
    Module defines a class MyInt that inherits from int
"""


class MyInt(int):
    """Class that inherits from class int"""
    def __eq__(self, other):
        """method to reverse == to !="""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """method to reverse != to =="""
        return int.__eq__(self, other)
