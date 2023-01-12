#!/usr/bin/python3
"""
    Module of a that appends a string to the end of a
    text file and returns number of characters.
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a
        text file and returns the number of characters added"""

    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
