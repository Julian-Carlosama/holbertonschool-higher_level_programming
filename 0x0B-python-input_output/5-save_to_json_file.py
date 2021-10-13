#!/usr/bin/python3
"""
Function that returns an object
(Python data structure) represented by a JSON string.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    by a JSON representationreturn the JSON representation
    """
    with open(filename, 'w', encoding="UTF8") as fd:
        return (json.dump(my_obj, fd))
