#!/usr/bin/python3
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
