#!/usr/bin/python3
"""
module: 0-lookup
resources: lookup function
"""


def lookup(obj):
    """
    Return list of available attributes and methods
    """
    return dir(obj)
