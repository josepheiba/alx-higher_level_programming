#!/usr/bin/python3
"""docs"""


class Rectangle:
    """docs"""
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """docs"""
        return self._width

    @width.setter
    def width(self, value):
        """docs"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self._width = value

    @property
    def height(self):
        """docs"""
        return self._height

    @height.setter
    def height(self, value):
        """docs"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self._height = value
