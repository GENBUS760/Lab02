#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time
import sys

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    #r = requests.get(url_1)
    #print("r status code", r.status_code)
    #print("r.json()", r.json())
    
    #for loop that pings the website 5 times
    for i in range(5):	
    	print("beginning iteration: ", i)
    	#ping the website and store response in variable "r"
    	r = requests.get(url_1)
    	#print("r status code type: ", r.status_code.type())
    	#if ping does not return 404 error, continue program execution
    	if(r.status_code!=404):
    		print("r status code did not equal 404, continuing...")
    		break
    	#if last iteration and still 404 error, end file
    	if(i==4 and r.status_code==404):
    		print("Attempted 5 iterations and failed, exiting program...")
    		sys.exit()
    	#try 5 times to get data
    	if r.status_code == "404":
    		print("On iteration number", i, " the status code was: ", r_status_code)	
	
    	
    	
    url_2 = "https://api.github.com/users/emaadmanzoor"
    r = requests.get(url_2)
    print(r.status_code)

    for key, value in r.json().items():
        print(key, value)

    print(r.headers)

    reset_time = r.headers["x-ratelimit-reset"]
    print("Rate limit resets at:", reset_time)

    remaining = r.headers["x-ratelimit-remaining"]
    print("API calls remaining:", remaining)

    current_time = time.time()
    reset_time = int(reset_time) # the API gives you a string, not an integer
    remaining_time = reset_time - current_time
    print("Remaining time (seconds)",
            remaining_time)

    print("Sleeping until reset...")
    time.sleep(remaining_time)
