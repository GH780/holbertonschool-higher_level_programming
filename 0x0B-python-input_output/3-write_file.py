#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Write a file with given string and returns the numbers of characters
        writed
    """
    with open(filename, "w", encoding="utf-8") as writer:
        return writer.write(text)
