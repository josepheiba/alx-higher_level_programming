#!/usr/bin/python3
"""docs"""


class Student:
    """docs"""

    def __init__(self, first_name, last_name, age):
        """docs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """docs"""
        return self.__dict__
