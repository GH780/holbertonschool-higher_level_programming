#!/usr/bin/python3
from models.rectangle import Rectangle
""" Square class inheris from Rectangle class
    class to create Square
"""


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor that uses the parameters of superclass Rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Method that returns string representation of square '''
        a, d = self.id, self.width
        b, c = self.x, self.y
        return("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
