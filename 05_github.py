#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    # r = requests.get(url_1)
    # print(r.status_code)
    # print(r.json())
    attempt = 3
    counter = 0

    print("Connecting to URL_1, Number of Attempt: 3")
    while counter < 3:
        try:
            r = requests.get(url_1)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            counter += 1
            print("Failed. Remaining attempt: " + str(attempt))
            attempt -= 1
            time.sleep(3)
        if(counter >= 3):
            print("Failed to connect to the Server, response internet status Error Code: " + str(r.status_code))
            exit_flag = 1

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
    print(current_time)
    reset_time = int(reset_time) # the API gives you a string, not an integer
    remaining_time = abs(reset_time - current_time)
    print("Remaining time (seconds)", remaining_time)

    if exit_flag == 1:
        print("Error exist.")
        exit(1)
        
    print("Sleeping until reset...")
    time.sleep(remaining_time)
