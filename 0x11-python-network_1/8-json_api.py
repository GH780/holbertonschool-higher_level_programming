#!/usr/bin/python3
import requests
from sys import argv
import json

q = ""
if len(argv) == 2:
    q = argv[1]

response = requests.post('http://0.0.0.0:5000/search_user', data = {'q': q})

try:
    dict = json.loads(response.text)
    if any(dict):
        print("[{}] {}".format(dict['id'], dict['name']))
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")
