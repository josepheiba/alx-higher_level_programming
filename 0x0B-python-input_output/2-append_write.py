#!/usr/bin/python3
"""docs"""


def append_write(filename="", text=""):
    """docs"""
    with open(filename, mode='a', encoding='utf-8') as fileObject:
        return fileObject.write(text)
