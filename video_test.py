import requests

BASE = "http://127.0.0.1:5000/"
headers = {"Content-Type": "application/json"}
# response = requests.put(BASE + "video/1", json={"likes": 10, "name": "Charles", "views": 100}, headers=headers)
# print(response.json())
# input() #waits for the user to press enter to input some data, acts like a pause
response = requests.get(BASE + 'video/6') #if a video_id that isn't in the videos dict is called, it will return the abort message  
print(response.json())