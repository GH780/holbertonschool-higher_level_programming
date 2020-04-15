#!/usr/bin/python3
import urllib.request as url
from sys import argv

response = url.urlopen(argv[1])
header = response.info()
print(header['X-Request-Id'])
