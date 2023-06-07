#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda x, y: x if x != search else y,
                    my_list, [replace] * len(my_list)))
