#!/usr/bin/python3
"""docs"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """docs"""

    def __init__(self, width, height):
        """docs"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """docs"""
        return self.__width * self.__height

    def __str__(self):
        """docs"""
        return f"[Rectangle] {self.__width}/{self.__height}"
