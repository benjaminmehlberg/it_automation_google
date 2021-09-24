#!/usr/bin/env python3
"""
A script to send images to a webserver
"""
import requests
import os

images_directory = os.path.expanduser("~/supplier-data/images")
url = "http://localhost/upload/"

os.chdir(images_directory)
dir_content = os.listdir()

for item in dir_content:
    with open(os.path.join(images_directory, item), "rb") as opened:
        request = requests.post(url, files={'file': opened})
