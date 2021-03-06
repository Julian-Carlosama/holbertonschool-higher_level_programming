#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    with statement is used.
    """
    with open(filename, "w", encoding="UTF8") as fd:
        return fd.write(text)
