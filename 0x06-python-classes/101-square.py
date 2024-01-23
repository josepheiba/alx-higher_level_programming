#!/usr/bin/python3
"""Define a class square."""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        area(): Returns the current square area.
        my_print(): Prints the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
