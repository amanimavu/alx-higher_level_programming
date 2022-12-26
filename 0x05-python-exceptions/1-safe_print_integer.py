#!/usr/bin/python3

'''program checks if a variable is an integer'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
