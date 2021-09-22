#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    
    for i in range(5):
    	s_code = r.status_code
    	if s_code == 404:
    		time.sleep(2)
    		i = i+1
    		print("this is an invalid URL, returns status code 404")
    	else:
    		print(r)
    

   
