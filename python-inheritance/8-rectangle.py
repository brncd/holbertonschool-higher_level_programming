#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
