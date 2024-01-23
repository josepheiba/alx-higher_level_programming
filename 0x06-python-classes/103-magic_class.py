#!/usr/bin/python3
"""Define a MagicClass"""


import math


class MagicClass:
    """Represent a circle."""
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return 2 ** self.__radius * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
