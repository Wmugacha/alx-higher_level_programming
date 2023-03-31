#!/usr/bin/python3
import urllib.request
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        html = response.read()
