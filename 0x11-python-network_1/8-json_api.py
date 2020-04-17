#!/usr/bin/python3
# Python script that fetches a url and post email using only requests
if __name__ == "__main__":
    import requests
    from sys import argv

    q = ""
    if len(argv) == 2:
        q = argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dict = response.json()
        if any(dict):
            print("[{}] {}".format(dict['id'], dict['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
