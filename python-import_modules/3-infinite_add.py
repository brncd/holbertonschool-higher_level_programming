#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if sys.argv[1:]:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        for i in range(3, len(sys.argv)):
            b += int(sys.argv[i])
        print("{}".format(a + b))
    else:
        print("0")
