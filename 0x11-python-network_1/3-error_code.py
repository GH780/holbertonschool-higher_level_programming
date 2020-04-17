#!/usr/bin/python3
# Python script to send request to URL and display error code
if __name__ == "__main__":
    import urllib.request as urr
    import urllib.error as ure
    from sys import argv

    try:
        with urr.urlopen(argv[1]) as response:
            response = response.read()
            print("{}".format(str(response, 'utf-8')))
    except ure.URLError as e:
        print("Error code: {}".format(e.code))
