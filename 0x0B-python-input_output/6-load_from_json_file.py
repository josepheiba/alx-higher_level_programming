#!/usr/bin/python3
"""docs"""


import json


def load_from_json_file(filename):
    """docs"""
    with open(filename, mode="r") as fileObject:
        line = fileObject.readline()

    return json.loads(line)
