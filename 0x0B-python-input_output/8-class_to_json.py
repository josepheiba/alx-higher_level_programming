#!/usr/bin/python3
"""docs"""


import json


def class_to_json(obj):
    """docs"""
    return json.dumps(obj.__dict__)
