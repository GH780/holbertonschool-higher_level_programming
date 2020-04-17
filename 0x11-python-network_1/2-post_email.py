#!/usr/bin/python3
# Python script to PORT to URL
if __name__ == "__main__":
    import urllib.request as urr
    import urllib.parse as urp
    from sys import argv

    values = {'email': argv[2]}
    data = urp.urlencode(values)
    data = data.encode('ascii')
    url = urr.Request(argv[1], data)

    with urr.urlopen(url) as response:
        response = response.read()

    print("{}".format(str(response, 'utf-8')))
