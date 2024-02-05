#!/usr/bin/python3
"""docs"""


def add_attribute(obj, attribute, value):
    """docs"""

    if hasattr(obj, '__dict__'):
        if not hasattr(obj, attribute):
            setattr(obj, attribute, value)
        else:
            raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
