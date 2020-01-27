#!/usr/bin/python3
import json
""" Main class Base """


class Base:
    """ Definition of attributes and methods """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor and manager to id attribute """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns a Json representation of a Python object"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save file with Python objects converted to Json"""
        cadena = ""
        list_dic = []

        if list_objs:
            for i in list_objs:
                list_dic.append(i.to_dictionary())
                file_name = i.__class__.__name__

        file_name += ".json"
        with open(file_name, "w") as writer:
            writer.write(cls.to_json_string(list_dic))
