import requests
import time
if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    for i in range(5):
        r = requests.get(url_1)
        if r.status_code == 404:
            time.sleep(10)
            print("failure")
        else print("success")
            break
