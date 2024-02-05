#!/usr/bin/python3
"""docs"""


class BaseGeometry:
    """docs"""

    def area(self):
        """docs"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """docs"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
