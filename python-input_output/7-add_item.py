#!/usr/bin/python3
"""Load, add, save."""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Add item."""
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []
    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
