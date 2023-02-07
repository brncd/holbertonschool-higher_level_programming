#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ True if the object is an instance of a class that inherited"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
