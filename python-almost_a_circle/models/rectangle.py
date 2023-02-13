#!/usr/bin/python3
"""First Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    _width = 0
    _height = 0
    _x = 0
    _y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
