#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

def check(url):
	count = 0
	while True:
		for _ in range(5):
			r = requests.get(url)
			code = r.status_code
			if code == 404:
				count += 1
			else:
				print(code)
			if count == 5:
				print('wrong url')
		break


if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    check(url_1)      # Check URL




