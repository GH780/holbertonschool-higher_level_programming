#!/usr/bin/python3
import urllib.request as url

with url.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()

print("Body response:")
print("\t- type:{}".format(type(response)))
print("\t- content:{}".format(response))
print("\t- utf-8 content:{}".format(str(response, 'utf-8')))
