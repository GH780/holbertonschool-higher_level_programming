#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Returns true if the object is exactly an instance of the a_class """
    return issubclass(a_class, type(obj))
