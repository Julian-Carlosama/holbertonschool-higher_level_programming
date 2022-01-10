#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body Response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {(html)}")
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
