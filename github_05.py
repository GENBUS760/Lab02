import time
import requests

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    for i in range(5):
        r = requests.get(url_1)
        if r.status_code == 404:
            time.sleep(2)
            print("failed request!")

        else:
            print("successful request!")
            break
