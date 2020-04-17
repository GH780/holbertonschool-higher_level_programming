#!/usr/bin/python3
import urllib.request as ur
from sys import argv

with ur.urlopen(argv[1]) as header:
    print(header.getheader('X-Request-Id'))
