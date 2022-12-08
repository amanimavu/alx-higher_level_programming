#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    new_dictionary = dict(a_dictionary)
    return new_dictionary
