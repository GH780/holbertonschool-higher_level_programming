#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = "argument" if len(sys.argv) == 2 else "arguments"
    print(len(sys.argv) - 1, "{} ".format(argument))
    for i in range(1, len(sys.argv)):
        print("{}: ".format(i), str(sys.argv[i]))
