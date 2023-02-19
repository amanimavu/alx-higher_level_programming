#!/usr/bin/python3

"""
module: base
resources: class Base, which is the base class of all class
in this project
"""
import json


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

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_list_objs = []
        for item in list_objs:
            new_list_objs.append(item.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        file_contents = Base.to_json_string(new_list_objs)
        with open(filename, 'w') as file:
            file.write(file_contents)

    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        list_of_instances = []
        filename = "{}.json".format(cls.__name__)
        with open(filename) as file:
            # str_list_of_dict - is a json string representation of
            # a list of str_list_of_dict - is a json string
            # representation of a list of dictionaries containing
            # instances variables(fields) with their values
            str_list_of_dict = file.read()
        list_output = cls.from_json_string(str_list_of_dict)
        for dictionary in list_output:
            list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
