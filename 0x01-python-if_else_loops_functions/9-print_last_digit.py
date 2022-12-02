#!/usr/bin/python3
def print_last_digit(number):
    abs_value = abs(number)
    last_digit = abs_value % 10

    print(last_digit, end="")
    return(last_digit)
