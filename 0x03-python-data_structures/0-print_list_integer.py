#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if not my_list:
        print("")
    else:
        for i in my_list:
            print("{}".format(i))
