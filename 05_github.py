#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    print('The error code appears to be: ' + str(r.status_code))
    print('\n')
    print(r.json())
    print('\n')
    print("Let's try again...")

    for x in range(0,6):
        print('Attempt #'+ str(x))
        status = r.status_code
        if status != 200:
            print('The error code is still ' + str(status) + '.')
            seconds = 2
            print("Let's wait", seconds, "seconds and try again")
            time.sleep(seconds)
        else:
            print('Wait it actually worked!')
            break
        print('Looks like we still get an error code of', str(status))

    
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


#Challenge Lab 1
#Determine error code
#If request fails, pause code using time.sleep and retry
#Determine the amount of retries
#Code should fail, but output is an error message


#Challenge Lab 2
#Use boto3 python library to create buckets in S3 and push any data through