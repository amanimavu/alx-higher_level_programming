#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    len_of_argv = len(argv) - 1
    if len_of_argv == 1:
        print("{} argument:".format(len_of_argv))
    elif len_of_argv == 0:
        print("{} arguments".format(len_of_argv))
        return None
    else:
        print("{} arguments:".format(len_of_argv))
    for i in range(1, len_of_argv + 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
