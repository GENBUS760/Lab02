#!/usr/bin/env python

import requests
import time

url_1= "https://api.github.com/emaadmanzoor"
rounds = 0

while rounds < 10:
  r = requests.get(url_1)
  stacode = r.status_code
  if stacode == 403:
  	print("the status code is", r.status_code)
  	break
  else:
  	rounds = rounds + 1
  	print ("Tried", rounds, "rounds and the status code is", stacode) 

time.sleep(1) 
print ("This is an invalid URL which return status code 404 after 10-round trial")
