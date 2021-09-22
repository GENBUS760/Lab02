import requests
import time 

r = requests.get("https://api.github.com/juliuswiscmsba")
  
remaining = r.headers["X-RateLimit-Remaining"]
reset_time = r.headers["X-RateLimit-Reset"]

current_time = time.time()
reset_time = int(reset_time)
remaining_time = reset_time - current_time
print("Remaining time (seconds)", remaining_time)

time.sleep(remaining_time)
