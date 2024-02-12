#!/usr/bin/python3
"""docs"""
import json


class Base:
    """docs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """docs"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """docs"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries or [])
