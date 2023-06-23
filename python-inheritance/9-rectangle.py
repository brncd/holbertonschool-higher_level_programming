#!/usr/bin/python3
"""Empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
