#!/usr/bin/python3
"""docs"""


def read_file(filename=""):
    """docs"""
    with open(filename, mode='r', encoding='utf-8') as fileObject:
        lines = fileObject.readlines()

    for line in lines:
        print(line, end="")
