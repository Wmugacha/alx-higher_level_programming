#!/usr/bin/python3
"""
   Module of a function that creates an Object from a “JSON file.
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file"""

    with open(filename) as myFile:
        return json.load(myFile)
