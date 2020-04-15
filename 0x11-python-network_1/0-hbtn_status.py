#!/usr/bin/python3
import urllib.request as url

with url.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()

print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(response),
                                                             response))
print('\t- utf8 content: {}'.format(str(response, 'utf-8')))
