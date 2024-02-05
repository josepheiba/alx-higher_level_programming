#!/usr/bin/python3
"""docs"""


def add_attribute(obj, attribute, value):
    """docs"""

    if isinstance(obj, object):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
