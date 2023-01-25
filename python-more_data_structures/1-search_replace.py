#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = lambda x, y: x if x != search else y
    return list(map(a, my_list, [replace] * len(my_list)))

