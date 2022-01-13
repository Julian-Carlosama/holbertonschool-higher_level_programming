#!/usr/bin/python3
""" Script that fetches a website """


import requests


if __name__ == "__main__":
    requ = requests.get('https://intranet.hbtn.io/status')
    print('Body Response:')
    print('\t- type:', type(requ.text))
    print('\t- content:', requ.text)
