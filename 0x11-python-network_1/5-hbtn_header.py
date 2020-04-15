#!/usr/bin/python3
import requests 
from sys import argv

response = requests.get(argv[1])
h = response.headers.get('X-Request-Id')
print(h)
