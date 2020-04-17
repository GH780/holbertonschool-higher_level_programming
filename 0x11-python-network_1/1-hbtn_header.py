#!/usr/bin/python3
# Python script that displays getheader value
if __name__ == '__main__':
    import urllib.request as url
    from sys import argv

    response = url.urlopen(argv[1])
    header = response.info()
    print(header['X-Request-Id'])
