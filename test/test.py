from rich.pretty import pprint
import requests

BASE_URL = 'http://127.0.0.1:5000/'

# response = requests.get(BASE_URL + "hts/all")
# pprint(response.json())
# response = requests.get(BASE_URL + "hts/div001")
# pprint(response.json())
response = requests.get(BASE_URL + "hts/div002")
pprint(response.json())
input()
response = requests.put(BASE_URL + "hts/div001", {
    "dateTime": "04/11/2021 20:30",
    "tempC": 23,
    "tempF": 456,
    "hum": 40,
    "sm": 56
})
pprint(response.json())
input()
response = requests.put(BASE_URL + "hts/div002", {
    "dateTime": "04/11/2021 20:35",
    "tempC": 23,
    "tempF": 456,
    "hum": 40,
    "sm": 56
})
pprint(response.json())
input()
response = requests.put(BASE_URL + "hts/div001", {
    "dateTime": "04/11/2021 20:40",
    "tempC": 23,
    "tempF": 456,
    "hum": 40,
    "sm": 56
})
pprint(response.json())
input()
response = requests.get(BASE_URL + "hts/div002")
pprint(response.json())
