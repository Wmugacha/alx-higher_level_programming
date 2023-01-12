#!/usr/bin/python3
"""
    Module of a function that inserts a line of text to a file,
    after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string"""

    with open(filename, 'r') as myfile:
        lines = myfile.readlines()
    with open(filename, 'w') as myfile:
        for line in lines:
            myfile.write(line)
            if search_string in line:
                myfile.write(new_string)
