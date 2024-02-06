#!/usr/bin/python3
"""docs"""


def write_file(filename="", text=""):
    """docs"""
    with open(filename, mode='w', encoding='utf-8') as fileObject:
        return fileObject.write(text)
