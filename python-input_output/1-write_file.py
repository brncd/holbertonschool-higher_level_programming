#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
