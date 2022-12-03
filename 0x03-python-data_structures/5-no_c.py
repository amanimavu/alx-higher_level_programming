#!/usr/bin/python3

# create a modified string without letter c
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
