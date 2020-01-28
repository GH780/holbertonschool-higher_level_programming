#!/usr/bin/python3
""" Main class Base """
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a Json representation of a Python object"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns a Json representation of a Python object """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance using update and its args and the values of
            a dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Create an instance using update and its args and the values of
            a dictionary.
        """
        list_obj = []
        if os.path.isfile(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r") as Reader:
                for i in Reader:
                    obj_py = cls.from_json_string(i)
                    for j in obj_py:
                        list_obj.append(cls.create(**j))

        return list_obj
