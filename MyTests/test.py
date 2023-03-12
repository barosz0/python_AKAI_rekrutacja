# import requests

base = "usd"
target = "EUR"

# url = f'https://api.exchangerate.host/convert?from={base}&to={target}'
# response = urllib.request.get(url)
# data = response.json()

# rate = data['info']['rate']
# date = data['date']
# print(date)
import json, datetime, urllib.request

url = f'https://api.exchangerate.host/convert?from={base}&to={target}'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

rate = data['info']['rate']
date = data['date']
print(data)

# print(data)
d = {"data":[{"base_currency":base, "target_currency": target, "date_fetched": date, "ratio": rate}]}

with open('json_data.json', 'w') as outfile:
    json.dump(d, outfile, indent=4)
    # outfile.write(json_string)



with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)