#!/usr/bin/python3
""" Square class inheris from Rectangle class
    class to create Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Definition of own methods and attributes """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor that uses the parameters of superclass Rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Method that returns string representation of square '''
        a, d = self.id, self.width
        b, c = self.x, self.y
        return("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        """ It allows don´t have a fixed number of arguments """
        if args:
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with every attribute of the
            Rectangle class
        """
        dic_squa = {"x": self.x, "y": self.y, "id": self.id,
                    "size": self.width}
        return dic_squa

    @property
    def size(self):
        """ Getter to size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter to size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
