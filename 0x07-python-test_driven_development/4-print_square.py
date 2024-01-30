#!/usr/bin/python3
"""Module print_square"""


def print_square(size):
    """size is the length of the square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
