#!/usr/bin/python3
"""docs"""


class BaseGeometry:
    """docs"""

    def area(self):
        """docs"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """docs"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
