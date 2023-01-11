#!/usr/bin/python3
"""
    Function that adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """method to add attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
