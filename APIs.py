import requests
import json

baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'012993441012'}
response = requests.get(baseURL, params=parameters)

content = response.content
info = json.loads(content)
print(type(info))
print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

print(title)
print(brand)
