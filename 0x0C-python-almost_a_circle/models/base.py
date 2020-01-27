#!/usr/bin/python3
import json
""" Main class Base """


class Base:

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
