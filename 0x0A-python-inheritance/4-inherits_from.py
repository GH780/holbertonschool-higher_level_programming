#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Returns true if the object is exactly an instance of the a_class
        or an instance of the superclass
    """
    if isinstance(obj, a_class) and issubclass(a_class, type(obj)):
        return False
    else:
        return True
