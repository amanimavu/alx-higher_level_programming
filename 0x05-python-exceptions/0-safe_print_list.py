#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(0, x + 1):
        try:
            num = int(my_list[i])
        except (ValueError, TypeError, IndexError):
            break
        else:
            print(num, end="")

    print("")
    return (i)
