#!/usr/bin/python3
def number_of_lines(filename=""):
    a = 0
    with open(filename, "r") as reader:
        for line in reader:
            a += 1

    return a
