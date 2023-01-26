#!/usr/bin/python3
"""
module: 2-is_name_class
resources: is_same_class function
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    return False
