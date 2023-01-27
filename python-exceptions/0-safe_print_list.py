#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list):
            x = len(my_list)
        for i in my_list:
            if i <= x:
                print("{}".format(i), end="")
        print()
        return x
    except IndexError:
        print()
        return i
