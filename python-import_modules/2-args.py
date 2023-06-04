#!/usr/bin/python3
#from sys import argv
#if __name__ == "__main__":
#    args = argv[1:]
#    print(len(args), "argument" if len(args) <= 1 else "arguments", end="")
#    print("." if len(args) == 0 else ":")
#    for idx, arg in enumerate(args, start=1):
#        print(idx, ":", arg)
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    print("{:d} argument{}".format(num, "" if num == 1 else "s"), end="")
    print("{}".format("." if num == 0 else ":"))
    if num > 0:
        for i in range(1, num + 1):
            print("{:d}: {}".format(i, argv[i]))
