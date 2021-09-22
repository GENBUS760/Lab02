#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    #print(r.status_code)
    #print(r.json())
    
    a=5
    while a>0 :
     if r.status_code != 200:
      time.sleep(3)
      r = requests.get(url_1)
      a=a-1
      print(r.status_code)
      if a == 0:
      	print(r.json()["message"])
     else:
      print(r.json())
      break
