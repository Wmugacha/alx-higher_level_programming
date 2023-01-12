#!/usr/bin/python3
"""
    Module of a function that returns the JSON
    representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""

    return json.JSONEncoder().encode(my_obj)
