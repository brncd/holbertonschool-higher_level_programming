#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """ Func returns True if obj is instance of specified class or inherited from it, else False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
