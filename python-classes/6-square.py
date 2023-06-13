#!/usr/bin/python3
"""Python - Classes and Objects"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square"""
        self.__size = size
        self.__position = position
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) and type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0) or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        return self.__position

    def area(self):
        """Return area"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
