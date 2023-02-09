#!/usr/bin/python3

"""
module: base
resources: class Base, which is the base class of all class
in this project
"""


class Base:
    """
    The goal of this class is to manage the id attribute in
    all the future classes of this project and to avoid code
    duplication (by extension, bug duplication)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
