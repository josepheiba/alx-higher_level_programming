#!/usr/bin/python3
"""docs"""


from models.base import Base


class Rectangle(Base):
    """docs"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """docs"""
        self.width = width
        self.height = height
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

    def display(self):
        """docs"""
        for _ in range(0, self.__y):
            print()
        for _ in range(0, self.__height):
            for _ in range(0, self.__x):
                print(" ", end="")
            for _ in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """docs"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """docs"""
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
