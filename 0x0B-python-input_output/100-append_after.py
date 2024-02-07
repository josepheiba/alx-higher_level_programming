#!/usr/bin/python3
"""docs"""


def append_after(filename="", search_string="", new_string=""):
    """docs"""
    with open(filename, "r") as fileObject:
        text = fileObject.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
