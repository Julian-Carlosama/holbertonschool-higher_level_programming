#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function that writes an object to a text file
    by a JSON representationreturn the JSON representation
    """
    with open(filename, 'r', encoding="UTF8") as fd:
        return (json.load(fd))
