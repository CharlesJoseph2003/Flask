import requests

BASE = "http://127.0.0.1:5000/"
headers = {"Content-Type": "application/json"}
response = requests.put(BASE + "video/1", json={"likes": 10}, headers=headers)
print(response.json())