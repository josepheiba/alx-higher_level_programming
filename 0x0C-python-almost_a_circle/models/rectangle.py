#!/usr/bin/python3
"""docs"""


from models.base import Base


class Rectangle(Base):
    """docs"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """docs"""
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validator(self, 'width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validator(self, 'height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validator(self, 'x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validator(self, 'y', value)
        self.__y = value

    def validator(self, name, value):
        """docs"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be and integer")
        if name == 'width' or name == 'height':
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """docs"""
        return self.width * self.height
