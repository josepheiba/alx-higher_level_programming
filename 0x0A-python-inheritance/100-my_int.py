#!/usr/bin/python3
"""docs"""


class MyInt(int):
    """docs"""

    def __eq__(self, myint):
        """docs"""
        return super().__ne__(myint)

    def __ne__(self, myint):
        """docs"""
        return super().__eq__(myint)
