#!/usr/bin/python3
"""docs"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """docs"""
    def __init__(self, size, x=0, y=0, id=None):
        """docs"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """docs"""
        return "[Square] ({}) {}/{} - {}".format(
        self.id, self.x, self.y, self.width)
