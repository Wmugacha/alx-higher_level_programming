#!/usr/bin/python3
import urllib.request
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        resp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("utf-8")))
