#!/usr/bin/env python
import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time
iteration=0
if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    for i in range(5):
      r = requests.get(url_1)
      if r.status_code == 404:
        iteration+=1
    if iteration == 5:
      print('Wrong')   





