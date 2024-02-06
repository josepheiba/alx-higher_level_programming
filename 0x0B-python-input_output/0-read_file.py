#!/usr/bin/python3
"""docs"""


def read_file(filename=""):
    """docs"""
    with open(filename, 'r') as fileObject:
        lines = fileObject.readline()
    print(lines)
