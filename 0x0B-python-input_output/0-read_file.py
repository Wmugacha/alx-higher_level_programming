#!/usr/bin/python3
"""
    Function that reads a text file and prints
    it to stdout.
"""


def read_file(filename=""):
    """function definition to read and print a text file"""

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
