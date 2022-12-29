#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            integer = int(my_list[i])
        except IndexError:
            raise
        except (TypeError, ValueError):
            continue
        else:
            count += 1
            print("{:d}".format(integer), end="")
    print("")
    return (count)
