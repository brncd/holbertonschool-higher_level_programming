#!/usr/bin/python3
"""Empty class BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize Square"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Return area"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
