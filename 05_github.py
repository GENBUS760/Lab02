#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    
    n=5
    sleeptime = 3
    for i in range(1,n):
     if r.status_code != 200:
      time.sleep(sleeptime)
      r = requests.get(url_1)
      print("Now status:",r.status_code)
      
      if i == n-1:
       print("Oh no! Errorrrrrrrrrrrrrrrrr!")
       
     else:
      print("Nice!!!!!!!!!!!! Success!!!!!!!!!!!!")
      print(r.json())
