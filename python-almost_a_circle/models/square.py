#!/usr/bin/python3
"""And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square."""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
