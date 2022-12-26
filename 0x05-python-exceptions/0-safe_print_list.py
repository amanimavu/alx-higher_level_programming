#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            num = int(my_list[i])
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
        else:
            count += 1
            print(num, end="")

    print("")
    return (count)
