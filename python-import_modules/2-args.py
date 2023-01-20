#!/usr/bin/python3
import sys
print("{} arguments".format(len(sys.argv) - 1))
if len(sys.argv) > 0:
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
