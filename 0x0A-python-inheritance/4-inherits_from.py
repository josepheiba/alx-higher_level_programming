#!/usr/bin/python3
"""docs"""


def inherits_from(obj, a_class):
    """docs"""
    return isinstance(obj, a_class) and type(obj) != a_class
