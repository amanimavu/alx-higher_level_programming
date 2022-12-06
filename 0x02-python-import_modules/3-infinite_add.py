#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    len_of_argv = len(argv)
    sum_of_args = 0
    for i in range(1, len_of_argv):
        sum_of_args += int(argv[i])

    print("{}".format(sum_of_args))


if __name__ == "__main__":
    main()
