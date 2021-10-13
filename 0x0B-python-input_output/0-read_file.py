#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
and prints it to stdout.
"""


def read_file(filename=""):
    """
    with statement is used.
    """
    with open(filename, encoding='UTF8') as fd:
        read_tx = fd.read()
        print(read_tx, end="")
    fd.close()
