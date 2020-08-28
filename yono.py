import copy
import random
import requests
import string
import sys
import threading
from time import sleep
#4yEgLATRaf
ip_addresses = ['45.117.163.22:8080', '185.64.18.25:8080','103.250.166.4:6666', '36.37.98.113:8080', '36.91.128.66:8080', '58.96.152.69:8080']
if len(sys.argv) > 1:
    THREAD_COUNT = int(sys.argv[1])
else:
    THREAD_COUNT = 50

global i
i = 0
text = None
text_get_method = ""

REQUEST_URL = "http://onyolo.com/"
BASE_DATA = {"text": "", "cookie": "", "wording": ""}
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

# Get the ID for the YOLO
if len(sys.argv) > 2:
    REQUEST_URL += sys.argv[2] + "/message"
else:
    id = id = input("ID: ")
    REQUEST_URL += id + "/message"

# Double-check that the YOLO in question exists
r = requests.get(f"http://onyolo.com/m/{id}", headers=HEADERS)
if r.content == b"Not Found":
    print("The YOLO ID provided does not exist.")
    sleep(5)
    exit()

# Get the faked question for YOLO
if len(sys.argv) > 3:
    BASE_DATA["wording"] = sys.argv[3]
else:
    wording = input("question: ")
    BASE_DATA["wording"] = wording

# Get the message to spam
if len(sys.argv) > 4:
    text = sys.argv[4]
    if len(text.split("|")) > 1:
        text = text.split("|")
else:
    text = input("Spam (pipe with |): ")
    if len(text.split("|")) > 1:
        text = text.split("|")

# Interval
unique = False
if len(sys.argv) > 5:
    if sys.argv[5].lower() == "y":
        unique = True
else:
    unique = input("Add interval to keep all messages different? [y/N]: ")
    if unique.lower() == "y":
        unique = True

random.seed()
class Spam(threading.Thread):
    def run(self):
        global i
        while True:
            data = copy.copy(BASE_DATA)

            data["cookie"] = "".join(random.choices(string.ascii_lowercase + string.digits, k=22))

            data["text"] = text
            if type(text) is list:
                data["text"] = random.choice(text)
            if unique:
                data["text"] += f" {i}"
            try:
                proxy_index = random.choice(ip_addresses)
                proxy = {"http": "http://" +proxy_index}
                r = requests.post(REQUEST_URL, json=data, headers=HEADERS, proxies=proxy)
                print(f"Sending message: {data['text']} (Message #{i})")
                i+=1
            except:
                print("Proxy failed:")###will add proxy output

for j in range(THREAD_COUNT):
    Spam().start()
    sleep(0.03125)

