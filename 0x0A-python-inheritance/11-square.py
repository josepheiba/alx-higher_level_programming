#!/usr/bin/python3
"""docs"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """docs"""

    def __init__(self, size):
        """docs"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """docs"""
        return super().area()

    def __str__(self):
        """docs"""
        return f"[Square] {self.__size}/{self.__size}"
