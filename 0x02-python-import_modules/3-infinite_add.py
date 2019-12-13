#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0

    if len(argv) == 1:
        a = 0
    else:
        for i in range(1, len(argv)):
            a = a + int(argv[i])

    print("{:d}".format(a))
