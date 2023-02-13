#!/usr/bin/python3
"""First Rectangle."""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle."""
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    