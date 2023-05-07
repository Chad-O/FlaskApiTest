import requests

res1 = requests.get("https://bsalesapi.herokuapp.com/flights/1/passengers")



print(res1.json()["data"]["airplaneId"])