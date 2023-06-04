#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    print(len(args), "argument" if len(args) <= 1 else "arguments", end="")
    print("." if len(args) == 0 else ":")
    for idx, arg in enumerate(args, start=1):
        print(idx, ":", arg)
