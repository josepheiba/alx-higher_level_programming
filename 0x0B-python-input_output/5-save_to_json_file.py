#!/usr/bin/python3
"""docs"""


import json


def save_to_json_file(my_obj, filename):
    """docs"""
    with open(filename, mode="w") as fileOcject:
        fileOcject.write(json.dumps(my_obj))
