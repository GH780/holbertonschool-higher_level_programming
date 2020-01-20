#!/usr/bin/python3
class MyList(list):
    """ Mylist inheritance of list """

    def print_sorted(self):
        print(sorted(self))
