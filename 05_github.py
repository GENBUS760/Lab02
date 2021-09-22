#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
  url_1 = "https://api.github.com/emaadmanzoor"
  for i in range(5):
    r = requests.get(url_1)
    if r.status_code==200:
      print(r.status_code)
      print(r.json())
      break
    i+=1
    print('wrong')
    time.sleep(5)
  print('error')

