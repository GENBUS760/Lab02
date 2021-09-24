#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    s_code = r.status_code
    'Allow 5 retries if request fails'
    for tempt in range(5): 
    	print('Attempt {}, Status Code: {}'.format(tempt+1,s_code))
    	if s_code == 404:
    	    time.sleep(2)
    	    r = requests.get(url_1)
    	    s_code = r.status_code            
    print(r.json())
    print()
    print('Attemped 5 times. Access Failed')
    
    #url_2 = "https://api.github.com/users/emaadmanzoor"
    #r = requests.get(url_2)
    #print(r.status_code)

    #for key, value in r.json().items():
    #    print(key, value)

