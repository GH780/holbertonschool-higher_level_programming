#!/usr/bin/python3
# Python script that fetches a url and get header value using only requests
if __name__ == "__main__":
    import requests 
    from sys import argv

    response = requests.get(argv[1])
    h = response.headers.get('X-Request-Id')
    print(h)
