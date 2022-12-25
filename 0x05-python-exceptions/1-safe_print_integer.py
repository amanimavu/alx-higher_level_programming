#!/usr/bin/python3

'''program checks if a variable is an integer'''


def safe_print_integer(value):
    try:
        integer = int(value)
    except ValueError:
        return False
    else:
        print("{:d}".format(integer))
    return True
