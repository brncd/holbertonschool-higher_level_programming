#!/usr/bin/python3
"""Python - More Classes and Objects"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle."""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Return string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
