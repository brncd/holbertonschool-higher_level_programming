#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
