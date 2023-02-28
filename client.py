import requests
import json

url = "http://127.0.0.1:8000/results?wspolrzedne="
a = input()
h = input()
url = url + {a} + {h}
response = requests.post(url, headers={'Content-Type': 'application/json'})

print(json.loads(response.text)["message"])