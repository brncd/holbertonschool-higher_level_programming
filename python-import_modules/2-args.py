#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)) == 1:
        dot = "."
    else:
        dot = ":"
    if (len(sys.argv)) == 2:
        print("{} argument{}".format(len(sys.argv) - 1, dot))
    else:
        print("{} arguments{}".format(len(sys.argv) - 1, dot))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
