#!/usr/bin/python3
import requests 
from sys import argv

response = requests.post(argv[1], data = {'email': argv[2]})
print(response)
